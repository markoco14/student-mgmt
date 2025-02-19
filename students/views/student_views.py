from typing import List
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers.student_serializers import StudentSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from classes.models import ClassEntity
# from evaluation.models.evaluation_attribute_model import EvaluationAttribute
from students.models.student import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class StudentList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, format=None):
        students = Student.objects.all().order_by('last_name')

        # Fetch query parameters
        school = request.query_params.get('school', None)
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        age = request.query_params.get('age', None)
        gender = request.query_params.get('gender', None)

        class_entity = request.query_params.get('class_entity', None)

        # FOR PAGES BASED ON ATTENDANCE
        attendance = request.query_params.get('attendance', None)
        date = request.query_params.get('date', None)

        page = request.query_params.get('page', None)
        per_page = request.query_params.get('per_page', 15)

        # Filter by school (hierachical url)
        if school:
            students = students.filter(school_id=school)

        # Further filter by query params
        if first_name:
            students = students.filter(first_name=first_name)
        if last_name:
            students = students.filter(last_name=last_name)
        if age:
            students = students.filter(age=age)
        if gender:
            students = students.filter(gender=gender)

        if class_entity:
            students = students.filter(class_students__class_id=class_entity)

        if attendance and date:
            students = students.filter(attendance__status__in=[
                                       0, 1]).filter(attendance__date=date)

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
                'next': students.next_page_number() if students.has_next() else None,
                'previous': students.previous_page_number() if students.has_previous() else None,
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
