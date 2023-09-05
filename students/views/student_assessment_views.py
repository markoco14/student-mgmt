from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from students.models.student_assessment_model import StudentAssessment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.serializers.student_assessment_serializers import StudentAssessmentDetailSerializer, StudentAssessmentSerializer

class StudentAssessmentList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, student_pk=None, format=None):
        student_assessments = StudentAssessment.objects.all()

        # Fetch query parameters
        # date = request.query_params.get('date', None)
        # author = request.query_params.get('author', None)
        # status = request.query_params.get('status', None)
        # reason = request.query_params.get('reason', None)
        # school_class = request.query_params.get('school_class', None)
        details = request.query_params.get('details', None)
        
        # # page = request.query_params.get('page', None)
        # per_page = request.query_params.get('per_page', 15)

        # Filter by school (hierachical url)
        if student_pk:
            student_assessments = student_assessments.filter(student_id=student_pk)

        # Further filter by query params
        # if date:
        #     student_assessments = student_assessments.filter(date=date)
        # if author:
        #     student_assessments = student_assessments.filter(author_id=author)
        # if status:
        #     student_assessments = student_assessments.filter(status=status)
        # if reason:
        #     student_assessments = student_assessments.filter(reason__contains=reason)
        # if school_class:
        #     student_assessments = student_assessments.filter(student_id__class_students__class_id=school_class)
        
        if details:
            serializer = StudentAssessmentDetailSerializer(student_assessments, many=True)
            return Response(serializer.data)


        serializer = StudentAssessmentSerializer(student_assessments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentAssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAssessmentDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, student_assessment_pk):
        try:
            return StudentAssessment.objects.get(id=student_assessment_pk)
        except StudentAssessment.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, student_assessment_pk):
        student_assessment = self.get_object(student_assessment_pk)
        serializer = StudentAssessmentSerializer(student_assessment)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, student_assessment_pk):
        student_assessment = self.get_object(student_assessment_pk)
        serializer = StudentAssessmentSerializer(student_assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, student_assessment_pk):
        student_assessment = self.get_object(student_assessment_pk)
        serializer = StudentAssessmentSerializer(
            student_assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_assessment_pk):
        student_assessment = self.get_object(student_assessment_pk)
        student_assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
