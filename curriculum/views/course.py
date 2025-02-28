from typing import List
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from curriculum.models import Course
from curriculum.models.level import Level
from curriculum.models.subject import Subject
from curriculum.serializers.course import CourseSerializer
from schools.models import SchoolUser
from users.models import User

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_courses(request) -> List[Course]:
    """
    Returns a list of courses.
    Query Params:
        - school: returns list of courses for given school
    """
    school = request.query_params.get("school")
    if not school:
        if not request.user.is_superuser:
            return Response({"detail": "Access denied."})
    
        courses = Course.objects.all()
    else:
        school_user = SchoolUser.objects.filter(user=request.user.id).filter(school__slug=school).first()
        if not school_user:
            return Response({"detail": "You don't have permission to list these classes"}, status=status.HTTP_403_FORBIDDEN)

        courses = Course.objects.filter(subject__school=school_user.school).all()

    courses_serializer = CourseSerializer(courses, many=True)

    return Response(courses_serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def new_course(request) -> Course:
    """
    Creates a new course and returns the row.
    Body Params:
        - 
    """
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=request.data["schoolID"]).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    course_serializer = CourseSerializer(data=request.data)

    if course_serializer.is_valid():
        course_serializer.save()
    else:
        return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"detail": "You made a new course."}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_course(request, course_pk) -> Course:
    """
    Returns a course for the given course id
    """
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
    
    course = get_object_or_404(Course, id=course_pk)
    
    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=course.subject.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    course_serializer = CourseSerializer(course, many=False)

    return Response(course_serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_course(request, course_pk) -> Course:
    """
    Updates a course record and returns updated record.
    """
    # only allow with owner membership for now, later need to allow staff
    if request.user.membership != User.MEMBERSHIP_OWNER:
        return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
    
    course = get_object_or_404(Course, id=course_pk)

    # we need to only allow if the user has access, regardless of membership
    school_user = SchoolUser.objects.filter(user=request.user.id).filter(school=course.subject.school).first()
    if not school_user:
        return Response({"detail": "No access granted."})
    
    subject = request.data.get("subject", None)
    if subject:
        try:
            db_subject = Subject.objects.get(id=subject)
            course.subject = db_subject
        except Subject.DoesNotExist:
            return Response({"detail": "Unable to find subject."}, status=status.HTTP_404_NOT_FOUND)
        
    level = request.data.get("level", None)
    if level:
        try:
            db_level = Level.objects.get(id=level)
            course.level = db_level
        except Level.DoesNotExist:
            return Response({"detail": "Unable to find level."}, status=status.HTTP_404_NOT_FOUND)

    try:
        course.save()
    except Exception as e:
        print(f"Error updating course {course.id}: {e}")
        return Response({"detail": "Something went wrong when updating the course record. Please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    course_serializer = CourseSerializer(course, many=False)

    return Response(course_serializer.data)