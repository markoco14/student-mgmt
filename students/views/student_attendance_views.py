from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from students.models.student_attendence import StudentAttendance
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.serializers.student_attendance import StudentAttendanceSerializer

# Create your views here.


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

        # check if page number is letters and send response that can be alerted
        # even though the front end should control for this.
        

        # if page is not None:

        #     try:
        #         page = int(page)
        #     except ValueError:
        #         return Response({"detail": "Page number needs to be an integer greater than 0"})
            

        #     paginator = Paginator(student_attendances, per_page)

        #     try:
        #         student_attendances = paginator.page(page)
        #     except PageNotAnInteger:
        #         student_attendances = paginator.page(1)
        #     except EmptyPage:
        #         student_attendances = paginator.page(paginator.num_pages)

        #     serializer = StudentAttendanceSerializer(student_attendances, many=True)

        #     return Response({
        #         'count': paginator.count,
        #         'total_pages': paginator.num_pages,
        #         'current_page': int(page),
        #         'per_page': int(per_page),
        #         'next': student_attendances.next_page_number() if student_attendances.has_next() else None,
        #         'previous': student_attendances.previous_page_number() if student_attendances.has_previous() else None,
        #         'results': serializer.data
        #     })

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        student_attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
