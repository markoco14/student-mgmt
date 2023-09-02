from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers.serializers import StudentSerializer
from rest_framework.exceptions import NotFound
from students.models.student import Student

# Create your views here.
class StudentList(APIView):
    """
    List all Units, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        modules = Student.objects.all()

        # Fetch query parameters
        # school = request.query_params.get('school', None)
        # subject = request.query_params.get('subject', None)
        # level = request.query_params.get('level', None)

        # Filter by school
        if school_pk:
            modules = modules.filter(school=school_pk)

        # # Further filter by subject if provided (use subject name)
        # if subject:
        #     modules = modules.filter(subject_level__subject__name=subject)

        # # Further filter by level if provided (use level order)
        # if level:
        #     modules = modules.filter(subject_level__level__order=level)

        serializer = StudentSerializer(modules, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, student_pk):
        try:
            return Student.objects.get(id=student_pk)
        except Student.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_pk):
        student = self.get_object(student_pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)