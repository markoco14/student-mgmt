"""
holds all subject related api views
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from curriculum.models.level_model import Level
from curriculum.models.subject_model import Subject
from curriculum.serializers.curriculum_serializers import LevelSerializer, SubjectSerializer
from schools.models import SchoolUser
from users.models import User


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_subjects(request):
    """
    Returns a list of subjects.
    Secrity:
        - No school filter? Only internal user.
    Params:
        - school: returns a list of subjects for given school.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    school = request.query_params.get("school")
    if not school:
        if not request.user.is_superuser:
            return Response({"detail": "Access denied"})
        
        subjects = Subject.objects.all()
    else:
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school__slug=school).first()
        if not school_user:
            return Response({"detail": "You don't have permission to list subjects at this school."}, status=status.HTTP_401_UNAUTHORIZED)
        
        subjects = Subject.objects.filter(school=school_user.school).all()

    subject_serializer = SubjectSerializer(subjects, many=True)

    return Response(subject_serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_subject(request):
    """
    Save a new subject for the school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=request.data["schoolID"]).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    subject_serializer = SubjectSerializer(data=request.data)

    if subject_serializer.is_valid():
        subject_serializer.save()
    else:
        return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(subject_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_subject(request, subject_pk):
    """
    Returns a subject.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        subject = Subject.objects.get(id=subject_pk)
    except Subject.DoesNotExist:
        raise NotFound(detail="Object with this ID not found.")

    school_user = SchoolUser.objects.filter(use=request.user.id).filter(school=subject.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    subject_serializer = SubjectSerializer(subject, many=False)

    return Response(subject_serializer.data)
