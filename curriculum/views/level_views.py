"""
holds all level related api views
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curriculum.models.level import Level
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

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_level(request, level_pk):
    """
    Show level details
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    try:
        level = Level.objects.filter(id=level_pk).get()
    except Level.DoesNotExist:
        return Response({"detail": "Level not found."}, status=status.HTTP_404_NOT_FOUND)
    
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=level.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    level_serializer = LevelSerializer(level, many=False)

    return Response(level_serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_level(request, level_pk):
    """
    Save a new level for the school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    try:
        level = Level.objects.filter(id=level_pk).get()
    except Level.DoesNotExist:
        return Response({"detail": "Level not found."}, status=status.HTTP_404_NOT_FOUND)

    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=level.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})

    name = request.data.get("name", None)
    if name:
        level.name = name

    order = request.data.get("order", None)
    if order:
        level.order = order

    try:
        level.save()
    except Exception as e:
        return Response({"detail": "Something went wrong with our server. Please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    level_serializer = LevelSerializer(level, many=False)

    return Response(level_serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_level(request, level_pk):
    """
    Save a new level for the school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    try:
        level = Level.objects.filter(id=level_pk).get()
    except Level.DoesNotExist:
        return Response({"detail": "Level not found."}, status=status.HTTP_404_NOT_FOUND)

    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=level.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})

    try:
        level.delete()
    except Exception as e:
        return Response({"detail": "Something went wrong deleting the level."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"detail": "Success"}, status=status.HTTP_204_NO_CONTENT)