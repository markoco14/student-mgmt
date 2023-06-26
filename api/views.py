from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import Student
from school.models import School
from user.models import User
from .serializers import StudentSerializer, SchoolSerializer, UserSerializer

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
    schools = School.objects.filter(owner=pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response({"data": serializer.data, "status": 200})

# ADD NEW SCHOOL


@api_view(['POST'])
def addSchool(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response({"data": serializer.data, "status": 200})

# DELETE SCHOOL


@api_view(['DELETE'])
def deleteSchool(request, pk):
    school = School.objects.get(id=pk)
    school.delete()

    return Response({"message": "School deleted.", "status": 204})

# UPDATE SCHOOL


@api_view(['POST'])
def updateSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(instance=school, data=request.data)
    if serializer.is_valid():
        serializer.save()

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

    return Response('Item successfully deleted!')
