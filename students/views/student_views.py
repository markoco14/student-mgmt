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
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        age = request.query_params.get('age', None)
        gender = request.query_params.get('gender', None)

        # Filter by school (hierachical url)
        if school_pk:
            modules = modules.filter(school=school_pk)

        # Further filter by query params
        if first_name:
            modules = modules.filter(first_name=first_name)
        if last_name:
            modules = modules.filter(last_name=last_name)
        if age:
            modules = modules.filter(age=age)
        if gender:
            modules = modules.filter(gender=gender)

      

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