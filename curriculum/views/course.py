from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from curriculum.models import Course
from curriculum.serializers.course import CourseSerializer
from schools.models import SchoolUser

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
