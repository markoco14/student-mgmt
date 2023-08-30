from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from curriculum.serializers.assessment_serializers import AssessmentSerializer, AssessmentTypeSerializer, ModuleAssessmentPageSerializer
from django.core.exceptions import FieldError
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from curriculum.models import Assessment, AssessmentType, Module

@api_view(['GET'])
def module_assessment_page_list(request, school_pk):
    modules = Module.objects.filter(subject_level__subject__school=school_pk).order_by('subject_level__subject__name', 'subject_level__level__order')
    serializer = ModuleAssessmentPageSerializer(modules, many=True)

    return Response(serializer.data)

class AssessmentTypeList(APIView):
    """
    List all Assessment Types, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        assessment_types = AssessmentType.objects.all()

        # Filter by school
        if school_pk:
            assessment_types = assessment_types.filter(school=school_pk)

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
    


class AssessmentList(APIView):
    """
    List all Assessments, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        assessments = Assessment.objects.all()

        module = request.query_params.get('module', None)
        type = request.query_params.get('type', None)

        if school_pk:
            assessments = assessments.filter(module__subject_level__subject__school=school_pk)
        
        if module:
             assessments = assessments.filter(module=module)

        if type:
             assessments = assessments.filter(type=type)

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
        serializer = AssessmentSerializer(assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, assessment_pk):
        assessment = self.get_object(assessment_pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)