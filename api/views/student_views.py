from rest_framework.response import Response
from rest_framework.decorators import api_view
from students.models import Student
from ..serializers.serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination

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

@api_view(['GET'])
def listStudentsByClass(request, pk):
    students = Student.objects.filter(classstudent__class_id=pk)
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENTS BY SCHOOL ID


@api_view(['GET'])
def getStudentsBySchoolId(request, pk):
    students = Student.objects.filter(school_id=pk).order_by('last_name')

    paginator = PageNumberPagination()
    paginated_students = paginator.paginate_queryset(students, request)
    serializer = StudentSerializer(paginated_students, many=True)

    return paginator.get_paginated_response(serializer.data)

# GET STUDENTS BY CLASS ID
# @api_view(['GET'])
# def getStudentsByClassId(request, pk):
#     students = Student.objects.filter()

# CREATE NEW STUDENT


@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE STUDENT


@api_view(['PUT'])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(
        instance=student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE STUDENT


@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response({"message": "Student successfully deleted."})