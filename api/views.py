from rest_framework.response import Response
from rest_framework.decorators import api_view
from student.models import Student
from core.models import School
from .serializers import StudentSerializer, SchoolSerializer

# GREETING VIEW
@api_view(['GET'])
def helloWorld(request):

    return Response("Hello World")

# SCHOOL VIEWS
@api_view(['GET'])
def listSchools(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

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

