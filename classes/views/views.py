"""
holds all classes related api views
"""
from typing import List

from rest_framework import status, request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from classes.models import ClassEntity
from classes.serializers import ClassEntitySerializer
from schools.models import SchoolUser
from schools.serializers import *
from students.models.student import Student
from students.serializers.serializers import StudentSerializer
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