from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from curriculum.serializers.assessment_serializers import AssessmentTypeSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from curriculum.models import AssessmentType

#

class AssessmentTypeList(APIView):
    """
    List all Units, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        assessment_types = AssessmentType.objects.all()

        # Fetch query parameters
        # school = request.query_params.get('school', None)
        # subject = request.query_params.get('subject', None)
        # level = request.query_params.get('level', None)

        # Filter by school
        if school_pk:
            assessment_types = assessment_types.filter(school=school_pk)

        # # Further filter by subject if provided (use subject name)
        # if subject:
        #     assessment_types = assessment_types.filter(subject_level__subject__name=subject)

        # # Further filter by level if provided (use level order)
        # if level:
        #     assessment_types = assessment_types.filter(subject_level__level__order=level)

        serializer = AssessmentTypeSerializer(assessment_types, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AssessmentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssessmentTypeDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, assessment_type_pk):
        try:
            return AssessmentType.objects.get(id=assessment_type_pk)
        except AssessmentType.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, assessment_type_pk):
        assessment_type = self.get_object(assessment_type_pk)
        serializer = AssessmentTypeSerializer(assessment_type)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, assessment_type_pk):
        assessment_type = self.get_object(assessment_type_pk)
        serializer = AssessmentTypeSerializer(assessment_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, assessment_type_pk):
        assessment_type = self.get_object(assessment_type_pk)
        serializer = AssessmentTypeSerializer(assessment_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, assessment_type_pk):
        assessment_type = self.get_object(assessment_type_pk)
        assessment_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)