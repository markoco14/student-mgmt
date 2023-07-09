from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from reports.models import Report
from students.models import Student
from schools.models import School
from classes.models import Class
from users.models import User
from .serializers import ReportSerializer, StudentSerializer, SchoolSerializer, UserSerializer, ClassSerializer
from django.db.models import Subquery

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# GREETING VIEW


@api_view(['GET'])
def helloWorld(request):

    return Response({"message": "Hello World"})

# USER VIEWS
# GET ALL USERS


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

# ADD NEW USER


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# SCHOOL VIEWS
# GET ALL SCHOOLS


@api_view(['GET'])
def getSchools(request, pk):
    schools = School.objects.filter(owner_id=pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)

# ADD NEW SCHOOL


@api_view(['POST'])
def addSchool(request):
    # return Response({"message": "hit the backend"})
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE SCHOOL


@api_view(['DELETE'])
def deleteSchool(request, pk):
    school = School.objects.get(id=pk)
    school.delete()

    return Response({"message": "School successfully deleted."})

# UPDATE SCHOOL


@api_view(['POST'])
def updateSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(instance=school, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# CLASS VIEWS
@api_view(['GET'])
def getClasses(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)

# STUDENT VIEWS
# GET ALL STUDENTS


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENT BY ID


@api_view(['GET'])
def getStudentById(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)

# GET STUDENTS BY OWNER ID


@api_view(['GET'])
def getStudentsByOwner(request, pk):
    students = Student.objects.filter(school_id__owner_id=pk)
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENTS BY SCHOOL ID


@api_view(['GET'])
def getStudentsBySchoolId(request, pk):
    students = Student.objects.filter(school_id=pk)
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


# CREATE NEW STUDENT
@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE STUDENT


@api_view(['POST'])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE STUDENT


@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response({"message": "Student successfully deleted."})

# REPORT ROUTES


@api_view(['GET'])
def getReportsAll(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getTodayReportByStudentId(request, pk):
    startdate = date.today()
    enddate = startdate + timedelta(days=1)

    report = Report.objects.filter(student_id=pk).filter(
        created_at__gte=startdate).filter(created_at__lt=enddate)
    serializer = ReportSerializer(report, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createReport(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateReport(request, pk):
    report = Report.objects.get(id=pk)
    serializer = ReportSerializer(instance=report, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteReport(request, pk):
    report = Report.objects.get(id=pk)
    report.delete()

    return Response({"message": "Report successfully deleted."})
