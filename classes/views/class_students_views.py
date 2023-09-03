from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import ClassStudent

from classes.serializers import ClassStudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

class ClassStudentList(APIView):
    """
    List all Classes, or create a new one.
    """

    def get(self, request, format=None):
        class_students = ClassStudent.objects.all()

        school_class = request.query_params.get('school_class', None)

        if school_class:
            class_students = class_students.filter(class_id=school_class)
        
        serializer = ClassStudentSerializer(class_students, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClassStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassStudentDetail(APIView):
    """
    Retrieve, update or delete a ClassStudent.
    """

    def get_object(self, class_student_pk):
        try:
            return ClassStudent.objects.get(id=class_student_pk)
        except ClassStudent.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, class_student_pk, format=None):
        class_student = self.get_object(class_student_pk)
        serializer = ClassStudentSerializer(class_student)
        return Response(serializer.data)

    def put(self, request, class_student_pk, format=None):
        class_student = self.get_object(class_student_pk)
        serializer = ClassStudentSerializer(class_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, class_student_pk):
        class_student = self.get_object(class_student_pk)
        serializer = ClassStudentSerializer(class_student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_student_pk, format=None):
        class_student = self.get_object(class_student_pk)
        class_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


