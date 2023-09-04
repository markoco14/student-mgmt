from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from students.models.student_attendence_model import StudentAttendance
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.serializers.student_attendance_serializers import StudentAttendanceDetailSerializer, StudentAttendanceSerializer

class StudentAttendanceList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        student_attendances = StudentAttendance.objects.all()

        # Fetch query parameters
        date = request.query_params.get('date', None)
        author = request.query_params.get('author', None)
        status = request.query_params.get('status', None)
        reason = request.query_params.get('reason', None)
        school_class = request.query_params.get('school_class', None)
        details = request.query_params.get('details', None)
        
        # # page = request.query_params.get('page', None)
        # per_page = request.query_params.get('per_page', 15)

        # Filter by school (hierachical url)
        if school_pk:
            student_attendances = student_attendances.filter(student_id__school_id=school_pk)

        # Further filter by query params
        if date:
            student_attendances = student_attendances.filter(date=date)
        if author:
            student_attendances = student_attendances.filter(author_id=author)
        if status:
            student_attendances = student_attendances.filter(status=status)
        if reason:
            student_attendances = student_attendances.filter(reason__contains=reason)
        if school_class:
            student_attendances = student_attendances.filter(student_id__class_students__class_id=school_class)
        
        if details:
            serializer = StudentAttendanceDetailSerializer(student_attendances, many=True)
            return Response(serializer.data)


        serializer = StudentAttendanceSerializer(student_attendances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAttendanceDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, student_attendance_pk):
        try:
            return StudentAttendance.objects.get(id=student_attendance_pk)
        except StudentAttendance.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        serializer = StudentAttendanceSerializer(student_attendance)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        serializer = StudentAttendanceSerializer(student_attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        serializer = StudentAttendanceSerializer(
            student_attendance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_attendance = serializer.save()
            updated_serializer = StudentAttendanceDetailSerializer(updated_attendance, many=False)
            return Response(updated_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        student_attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
