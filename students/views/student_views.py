from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers.serializers import StudentSerializer
from rest_framework.exceptions import NotFound
from students.models.student import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class StudentList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        students = Student.objects.all()

        # Fetch query parameters
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        age = request.query_params.get('age', None)
        gender = request.query_params.get('gender', None)
        page = request.query_params.get('page', None)
        per_page = request.query_params.get('per_page', 20)

        # Filter by school (hierachical url)
        if school_pk:
            students = students.filter(school=school_pk)

        # Further filter by query params
        if first_name:
            students = students.filter(first_name=first_name)
        if last_name:
            students = students.filter(last_name=last_name)
        if age:
            students = students.filter(age=age)
        if gender:
            students = students.filter(gender=gender)

        # check if page number is letters and send response that can be alerted
        # even though the front end should control for this.
        

        if page is not None:
            
            try:
                page = int(page)
            except ValueError:
                return Response({"detail": "Page number needs to be an integer greater than 0"})
            

            paginator = Paginator(students, per_page)

            try:
                students = paginator.page(page)
            except PageNotAnInteger:
                students = paginator.page(1)
            except EmptyPage:
                students = paginator.page(paginator.num_pages)

            serializer = StudentSerializer(students, many=True)

            return Response({
                'count': paginator.count,
                'total_pages': paginator.num_pages,
                'current_page': int(page),
                'per_page': int(per_page),
                'results': serializer.data
            })

        serializer = StudentSerializer(students, many=True)
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
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_pk):
        student = self.get_object(student_pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
