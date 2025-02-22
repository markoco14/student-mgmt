"""
holds all student related api views
"""
from typing import List

from rest_framework import status, request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from schools.models import SchoolUser
from schools.serializers import *
from students.models.student import Student
from students.serializers.serializers import StudentSerializer
from users.models import User



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_students(request: request) -> List[Student]:
    """
    Returns a list of students
    Security:
        - only authenticated users
        - if no school selected, only show internally (is_superuser for now, include is_admin later)
        - if school selected, only allow if user has access to that school
    Query params:
        - school: returns only students for that school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    school = request.query_params.get("school", None)
    
    # check if user has access to school
    if not school:
        if not request.user.is_superuser:
            return Response({"detail": "No access granted."})
        
        students = Student.objects.all()
    else:
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=school).first()
        if not school_user:
            return Response({"detail": "No access granted."})
        
        students = Student.objects.filter(school=school).all()
    

    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_student(request: request) -> Student:
    """
    Stores a new student in the database and returns the student model.
    Security:
        - only authenticated users
        - only owner membership for now, later allow staff
        - only if user (owner) has access permission to that school
    Body:
        first_name
        last_name
        age
        gender 0 = male and 1 = female
        photo_url** optional
        school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=request.data["school"]).first()
    if not school_user:
        return Response({"detail": "No access granted."})

    student_serializer = StudentSerializer(data=request.data)

    if student_serializer.is_valid():
        student_serializer.save()
    else:
        return Response({"detail": "Something is wrong with the request data"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(student_serializer.data)


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


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_student(request, student_pk):
    """
    Update a student's information.
    Security:
        - only allow authenticated
        - only allow owner membership
        - only if student exists
        - only allow those with school access is owner or admin
    Body **all optional:
        - first_name
        - last_name
        - age
        - gender 0 = male and 1 = female
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # check if student exists
    db_student = Student.objects.filter(id=student_pk).first()
    if not db_student:
        return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    # does the user have access to that student's school?
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=db_student.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    if db_student.first_name != request.data["first_name"]:
        db_student.first_name = request.data["first_name"]

    if db_student.last_name != request.data["last_name"]:
        db_student.last_name = request.data["last_name"]

    if db_student.age != request.data["age"]:
        db_student.age = request.data["age"]
    
    if db_student.gender != request.data["gender"]:
        db_student.gender = request.data["gender"]
    
    db_student.save()

    student_serializer = StudentSerializer(db_student, many=False)

    return Response(student_serializer.data)
   

