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
        - school: the school slug from the page url path, passed as query param
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
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school__slug=school).first()
        if not school_user:
            return Response({"detail": "No access granted."})
        
        students = Student.objects.filter(school__slug=school).all()
    

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
        firstName
        lastName
        age
        gender (0 = male and 1 = female)
        school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=request.data["schoolID"]).first()
    if not school_user:
        return Response({"detail": "No access granted."})

    student_data = request.data.copy()
    
    student_serializer = StudentSerializer(data=student_data)

    if student_serializer.is_valid():
        student_serializer.save()
    else:
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(student_serializer.data, status=status.HTTP_201_CREATED)


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
    Editable fields (optional):
        - firstName
        - lastName
        - age
        - gender 0 = male and 1 = female
        - photoUrl
    Uneditable fields:
        - school
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not request.data:
        return Response({"detail": "No data in request"}, status=status.HTTP_400_BAD_REQUEST)
    # check if student exists
    db_student = Student.objects.filter(id=student_pk).first()
    if not db_student:
        return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    # does the user have access to that student's school?
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=db_student.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    first_name = request.data.get("firstName", None)
    if first_name:
        db_student.first_name = request.data["firstName"]

    last_name = request.data.get("lastName", None)
    if last_name:
        db_student.last_name = request.data["lastName"]

    age = request.data.get("age", None)
    if age:
        db_student.age = request.data["age"]
    
    gender = request.data.get("gender", None)
    if gender:
        db_student.gender = request.data["gender"]

    photo_url = request.data.get("photoUrl", None)
    if photo_url:
        db_student.photo_url = request.data["photoUrl"]
    
    db_student.save()

    student_serializer = StudentSerializer(db_student, many=False)

    return Response(student_serializer.data)
   

