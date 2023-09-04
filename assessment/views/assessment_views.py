from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
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


class AssessmentDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, assessment_pk):
        try:
            return Assessment.objects.get(id=assessment_pk)
        except Assessment.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, assessment_pk):
        assessment = self.get_object(assessment_pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, assessment_pk):
        assessment = self.get_object(assessment_pk)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, assessment_pk):
        assessment = self.get_object(assessment_pk)
        serializer = AssessmentSerializer(
            assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, assessment_pk):
        assessment = self.get_object(assessment_pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
