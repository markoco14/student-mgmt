from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from curriculum.models import Course
from curriculum.serializers.course import CourseSerializer
from schools.models import SchoolUser
from users.models import User

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_courses(request):
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
def new_course(request):
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