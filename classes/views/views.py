"""
holds all classes related api views
"""
import ast

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from classes.models import ClassEntity
from classes.serializers import ClassEntitySerializer
from schools.models import SchoolUser
from users.models import User

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_classes(request):
    """
    Returns a list of classes.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    school = request.query_params.get("school")
    if not school:
        if not request.user.is_superuser:
            return Response({"detail": "Access denied."})
    
        classes = ClassEntity.objects.all()
    else:
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school__slug=school).first()
        if not school_user:
            return Response({"detail": "You don't have permission to list these classes"}, status=status.HTTP_401_UNAUTHORIZED)

        classes = ClassEntity.objects.filter(school=school_user.school).all()

    classes_serializer = ClassEntitySerializer(classes, many=True)

    return Response(classes_serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_class(request):
    """
    Creates a new class entity related to a given school.
    Security:
        - isuser authenticated
        - only owner membership for now
        - only if user (owner) has access permission to that school
    Request Body:
        - name
        - level
        - days
        - teacher
        - schoolID
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
    
    days_list = ast.literal_eval(request.data["days"])

    class_data = request.data.copy()
    class_data["days"] = days_list


    class_serializer = ClassEntitySerializer(data=class_data)

    if class_serializer.is_valid():
        class_serializer.save()
    else:
        return Response(class_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(class_serializer.data)
    

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_class(request, class_pk):
    """
    Update class information.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.data:
        return Response({"detail": "No data in request"}, status=status.HTTP_400_BAD_REQUEST)
    
    db_class = ClassEntity.objects.filter(id=class_pk).first()
    if not db_class:
        return Response({"detail": "Class not found."}, status=status.HTTP_404_NOT_FOUND)

    school_access = SchoolUser.objects.filter(user=request.user.id).filter(school=db_class.school)
    if not school_access:
        return Response({"detail": "You can't access classes for this school"})

    
    name = request.data.get("name", None)
    if name:
        db_class.name = name

    level = request.data.get("level", None)
    if level:
        db_class.level = level

    teacher = request.data.get("teacher", None)
    if teacher:
        db_class.teacher = teacher

    days = request.data.get("days", None)
    if days:
        days = ast.literal_eval(days)
        db_class.days = days

    school = request.data.get("schoolID", None)
    if school:
        db_class.school = school

    db_class.save()

    class_serializer = ClassEntitySerializer(db_class, many=False)
    
    return Response(class_serializer.data)
    
