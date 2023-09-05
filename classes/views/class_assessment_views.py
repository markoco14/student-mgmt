from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from classes.models import ClassAssessment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from classes.serializers import ClassAssessmentDetailSerializer, ClassAssessmentSerializer

class ClassAssessmentList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, class_pk=None, format=None):
        class_assessments = ClassAssessment.objects.all()

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
        if class_pk:
            class_assessments = class_assessments.filter(class_id=class_pk)

        # Further filter by query params
        # if date:
        #     class_assessments = class_assessments.filter(date=date)
        # if author:
        #     class_assessments = class_assessments.filter(author_id=author)
        # if status:
        #     class_assessments = class_assessments.filter(status=status)
        # if reason:
        #     class_assessments = class_assessments.filter(reason__contains=reason)
        # if school_class:
        #     class_assessments = class_assessments.filter(student_id__class_students__class_id=school_class)
        
        if details:
            serializer = ClassAssessmentDetailSerializer(class_assessments, many=True)
            return Response(serializer.data)


        serializer = ClassAssessmentSerializer(class_assessments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassAssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassAssessmentDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, class_assessment_pk):
        try:
            return ClassAssessment.objects.get(id=class_assessment_pk)
        except ClassAssessment.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, class_assessment_pk):
        class_assessment = self.get_object(class_assessment_pk)
        serializer = ClassAssessmentSerializer(class_assessment)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, class_assessment_pk):
        class_assessment = self.get_object(class_assessment_pk)
        serializer = ClassAssessmentSerializer(class_assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, class_assessment_pk):
        class_assessment = self.get_object(class_assessment_pk)
        serializer = ClassAssessmentSerializer(
            class_assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, class_assessment_pk):
        class_assessment = self.get_object(class_assessment_pk)
        class_assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
