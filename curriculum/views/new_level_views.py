"""
holds all classes related api views
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curriculum.models.level_model import Level
from curriculum.serializers.curriculum_serializers import LevelSerializer
from schools.models import SchoolUser
from users.models import User


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_levels(request):
    """
    Returns a list of classes.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    school = request.query_params.get("school")
    if not school:
        if not request.user.is_superuser:
            return Response({"detail": "Access denied."})
    
        levels = Level.objects.all()
    else:
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school__slug=school).first()
        if not school_user:
            return Response({"detail": "You don't have permission to list these classes"}, status=status.HTTP_401_UNAUTHORIZED)

        levels = Level.objects.filter(school=school_user.school).all()

    level_serializer = LevelSerializer(levels, many=True)

    return Response(level_serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_level(request):
    """
    Save a new level for the school
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
    
    level_serializer = LevelSerializer(data=request.data)

    if level_serializer.is_valid():
        level_serializer.save()
    else:
        return Response(level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(level_serializer.data)