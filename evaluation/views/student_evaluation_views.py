from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.exceptions import NotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from evaluation.models.student_evaluations import StudentEvaluation
from evaluation.serializers.student_evaluation_serializers import StudentEvaluationSerializer

class StudentEvaluationList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, student_pk=None, format=None):
        student_evaluations = StudentEvaluation.objects.all()

        # Fetch query parameters
        # date = request.query_params.get('date', None)
        # author = request.query_params.get('author', None)
        # status = request.query_params.get('status', None)
        # reason = request.query_params.get('reason', None)
        # school_class = request.query_params.get('school_class', None)
        # details = request.query_params.get('details', None)
        
        # # page = request.query_params.get('page', None)
        # per_page = request.query_params.get('per_page', 15)

        # Filter by school (hierachical url)
        if student_pk:
            student_evaluations = student_evaluations.filter(student_id=student_pk)

        # Further filter by query params
        # if date:
        #     student_evaluations = student_evaluations.filter(date=date)
        # if author:
        #     student_evaluations = student_evaluations.filter(author_id=author)
        # if status:
        #     student_evaluations = student_evaluations.filter(status=status)
        # if reason:
        #     student_evaluations = student_evaluations.filter(reason__contains=reason)
        # if school_class:
        #     student_evaluations = student_evaluations.filter(student_id__class_students__class_id=school_class)
        
        # if details:
        #     serializer = StudentEvaluationDetailSerializer(student_evaluations, many=True)
        #     return Response(serializer.data)


        serializer = StudentEvaluationSerializer(student_evaluations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentEvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentEvaluationDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, student_evaluation_pk):
        try:
            return StudentEvaluation.objects.get(id=student_evaluation_pk)
        except StudentEvaluation.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, student_evaluation_pk):
        student_evaluation = self.get_object(student_evaluation_pk)
        serializer = StudentEvaluationSerializer(student_evaluation)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, student_evaluation_pk):
        student_evaluation = self.get_object(student_evaluation_pk)
        serializer = StudentEvaluationSerializer(student_evaluation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, student_evaluation_pk):
        student_evaluation = self.get_object(student_evaluation_pk)
        serializer = StudentEvaluationSerializer(
            student_evaluation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_evaluation_pk):
        student_evaluation = self.get_object(student_evaluation_pk)
        student_evaluation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
