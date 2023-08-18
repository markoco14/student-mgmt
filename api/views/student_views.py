from rest_framework.response import Response
from rest_framework.decorators import api_view
from students.models import Student
from ..serializers.serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination

# GET ALL STUDENTS


@api_view(['GET'])
def listStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENT BY ID


@api_view(['GET'])
def getStudent(request, student_pk):
    student = Student.objects.get(id=student_pk)
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


@api_view(['PUT'])
def updateStudent(request, student_pk):
    student = Student.objects.get(id=student_pk)
    serializer = StudentSerializer(
        instance=student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE STUDENT


@api_view(['DELETE'])
def deleteStudent(request, student_pk):
    student = Student.objects.get(id=student_pk)
    student.delete()

    return Response({"message": "Student successfully deleted."})

# GET STUDENTS BY SCHOOL ID


@api_view(['GET'])
def listSchoolStudents(request, school_pk):
    students = Student.objects.filter(
        school_id=school_pk).order_by('last_name')

    paginator = PageNumberPagination()
    paginated_students = paginator.paginate_queryset(students, request)
    serializer = StudentSerializer(paginated_students, many=True)

    return paginator.get_paginated_response(serializer.data)

# GET STUDENTS BY CLASS ID


@api_view(['GET'])
def listClassStudents(request, class_pk):
    students = Student.objects.filter(classstudent__class_id=class_pk)
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)
