from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from assessment.serializers import assessment_serializer
from students.models.student_attendence_model import StudentAttendance
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from assessment.models.assessment_model import Assessment
from assessment.serializers.assessment_serializer import AssessmentSerializer


class AssessmentList(APIView):
    """
    List all Assessments, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        assessments = Assessment.objects.all()

        # Filter by school (hierachical url)
        if school_pk:
            assessments = assessments.filter(student_id__school_id=school_pk)
            
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentAttendanceDetail(APIView):

#     # Utility method to get an object or return a 404 response
#     def get_object(self, student_attendance_pk):
#         try:
#             return StudentAttendance.objects.get(id=student_attendance_pk)
#         except StudentAttendance.DoesNotExist:
#             raise NotFound(detail="Object with this ID not found.")

#     # Retrieve a specific entry by primary key
#     def get(self, request, student_attendance_pk):
#         student_attendance = self.get_object(student_attendance_pk)
#         serializer = Serializer(student_attendance)
#         return Response(serializer.data)

#     # Update a specific entry by primary key
#     def put(self, request, student_attendance_pk):
#         student_attendance = self.get_object(student_attendance_pk)
#         serializer = Serializer(student_attendance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Partially update a specific entry by primary key
#     def patch(self, request, student_attendance_pk):
#         student_attendance = self.get_object(student_attendance_pk)
#         serializer = Serializer(
#             student_attendance, data=request.data, partial=True)
#         if serializer.is_valid():
#             updated_attendance = serializer.save()
#             updated_serializer = StudentAttendanceDetailSerializer(updated_attendance, many=False)
#             return Response(updated_serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete a specific entry by primary key
#     def delete(self, request, student_attendance_pk):
#         student_attendance = self.get_object(student_attendance_pk)
#         student_attendance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
