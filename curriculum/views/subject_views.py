"""
holds all subject related api views
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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