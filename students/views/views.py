"""
holds all school related api views
"""
from typing import List
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status, request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from schools.models import School, SchoolDay, SchoolUser
from schools.serializers import *
from students.models.student import Student
from students.serializers.serializers import StudentSerializer
from users.models import Teacher



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_students(request: request) -> List[Student]:
    """
    Returns a list of students
    Query params:
        school - returns only students for that school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    school = request.query_params.get("school", None)
    
    # check if user has access to school
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    else:
        print(school_user)
    
    if not school:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(school=school).all()

    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_by_id(request, student_pk):
    """
    get a single school by id
    """
    try:
        student = Student.objects.get(id=student_pk)
    except Student.DoesNotExist:
        return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)
