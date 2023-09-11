from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from api.serializers.serializers import StudentSerializer
from students.models.student import Student
from students.models.student_attendence_model import StudentAttendance
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.serializers.student_attendance_serializers import StudentAttendanceDetailSerializer, StudentAttendanceSerializer, StudentWithAttendanceSerializer


@api_view(['GET'])
def get_students_with_attendance(request, school_pk=None):
    students = Student.objects.all()

    class_entity = request.query_params.get('class_entity', None)
    date = request.query_params.get('date', None)

    if class_entity:
        students = students.filter(class_students__class_id=class_entity)

    serializer = StudentWithAttendanceSerializer(students, many=True, context={'class_entity': class_entity, 'date': date})

    return Response(serializer.data)


@api_view(['GET'])
def get_students_here_today(request, school_pk=None):
    students = Student.objects.all()

    class_entity = request.query_params.get('class_entity', None)
    if class_entity:
        students = students.filter(class_students__class_id=class_entity)

    date = request.query_params.get('date', None)
    if date:
        students = students.filter(attendance__date=date)

    attendance = request.query_params.get('attendance', None)
    if attendance:
        students = students.filter(
            attendance__class_id=class_entity, attendance__status__in=[0, 1])
    # REMOVE DUPLICATES CAUSED BY ORM JOINS
    students = students.distinct()

    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_attendance_records_for_class_list(request):

    class_id = request.data['class_id']

    # CREATE HOLDER FOR ATTENDANCE RECORDS
    attendance_records = []

    for student in request.data['class_list']:
        attendance_record = {
            "student_id_id": student['student_id'],
            "class_id_id": class_id,
            "date": request.data['date'],
            "status": 0,
            "reason": None,
            "author_id_id": request.data['user_id'],
        }
        attendance_records.append(attendance_record)

    created_records = StudentAttendance.objects.bulk_create(
        [StudentAttendance(**record) for record in attendance_records])

    if created_records:
        # BECAUSE BATCH CREATE RETURNING NULL IDS = FRONTEND RENDERING PROBLEM
        fetched_records = StudentAttendance.objects.filter(
            date=request.data['date']).filter(class_id=class_id)

        serializer = StudentAttendanceDetailSerializer(
            fetched_records, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'detail': 'Attendance records created'}, status=status.HTTP_201_CREATED)


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
            student_attendances = student_attendances.filter(
                student_id__school_id=school_pk)

        # Further filter by query params
        if date:
            student_attendances = student_attendances.filter(date=date)
        if author:
            student_attendances = student_attendances.filter(author_id=author)
        if status:
            student_attendances = student_attendances.filter(status=status)
        if reason:
            student_attendances = student_attendances.filter(
                reason__contains=reason)
        if school_class:
            student_attendances = student_attendances.filter(
                class_id=school_class)

        if details:
            serializer = StudentAttendanceDetailSerializer(
                student_attendances, many=True)
            return Response(serializer.data)

        serializer = StudentAttendanceSerializer(
            student_attendances, many=True)
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
        serializer = StudentAttendanceSerializer(
            student_attendance, data=request.data)
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
            updated_serializer = StudentAttendanceDetailSerializer(
                updated_attendance, many=False)
            return Response(updated_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_attendance_pk):
        student_attendance = self.get_object(student_attendance_pk)
        student_attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
