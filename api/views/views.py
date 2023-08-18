from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from levels.models import Level
from reports.models import Report, ReportDetails
from students.models import Student
from schools.models import School, SchoolUser
from classes.models import Class, ClassStudent
from users.models import Teacher, User
from ..serializers.serializers import LevelSerializer, ReportDetailsSerializer, ReportSerializer, SchoolUserSerializer, StudentSerializer, SchoolSerializer, TeacherSerializer, UserSerializer, ClassSerializer, ClassStudentSerializer
from django.db.models import Subquery, Prefetch
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

# GREETING VIEW


@api_view(['GET'])
def helloWorld(request):

    return Response({"message": "Hello World"})
     

#
#
#
# SCHOOL USER ACCESS ROUTES
#
#
#
@api_view(['GET'])
def getSchoolsByUserAccess(request, pk):
    schools = School.objects.filter(school_users__user=pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)




