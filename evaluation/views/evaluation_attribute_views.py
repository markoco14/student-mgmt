from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import ProtectedError

from evaluation.models.evaluation_attribute_model import EvaluationAttribute, RangeEvaluationAttribute, TextEvaluationAttribute
from evaluation.serializers.evaluation_attribute_serializers import EvaluationAttributeListSerializer, EvaluationAttributeSerializer, RangeEvaluationAttributeSerializer, TextEvaluationAttributeSerializer

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView


# Create your views here.


@api_view(['GET'])
def get_daily_report_eval_attributes(request, school_pk=None):
    try:
        queryset = EvaluationAttribute.objects.select_related(
            'rangeevaluationattribute', 'textevaluationattribute').all().order_by('-data_type_id')

        # queryset = RangeEvaluationAttribute.objects.all()

        if school_pk:
            queryset = queryset.filter(school_id=school_pk)

        serializer = EvaluationAttributeSerializer(queryset, many=True)
        # serializer = RangeEvaluationAttributeSerializer(queryset, many=True)

        return Response(serializer.data)
    except EvaluationAttribute.DoesNotExist:
        return Response({"details": "No objects with that School ID found."})


# EVALUATION ATTRIBUTE VIEWS

class EvaluationAttributeList(APIView):
    """
    List all EvaluationAttributes, or create a new one.
    """

    def get(self, request, format=None):
        attributes = EvaluationAttribute.objects.all().order_by('-data_type_id')

        # Filter by school
        school = request.query_params.get('school')
        if school:
            attributes = attributes.filter(school_id=school)

        details = request.query_params.get('details', None)
        if details:
            serializer = EvaluationAttributeSerializer(attributes, many=True)
            return Response(serializer.data)

        serializer = EvaluationAttributeListSerializer(attributes, many=True)
        return Response(serializer.data)

    # CHECKS FOR CONDITIONAL RANGE OR TEXT
    # AND USES RANGE OR TEXT SERIALIZER
    # BECAUSE WE NEED TO CHOOSE TYPE
    def post(self, request, format=None):
        # CREATES RANGE TYPE
        if request.data['data_type_id'] == 0:
            serializer = RangeEvaluationAttributeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # CREATES TEXT TYPE
        if request.data['data_type_id'] == 1:
            serializer = TextEvaluationAttributeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvaluationAttributeDetail(APIView):
    """
    Retrieve, update or delete a EvaluationAttribute.
    """

    def get_object(self, evaluation_attribute_pk):
        try:
            return EvaluationAttribute.objects.get(id=evaluation_attribute_pk)
        except EvaluationAttribute.DoesNotExist:
            raise NotFound({"error": "We couldn't find this metric. Please try refreshing the page."})

    def get(self, request, evaluation_attribute_pk, format=None):
        evaluation_attribute = self.get_object(evaluation_attribute_pk)
        serializer = EvaluationAttributeSerializer(evaluation_attribute)
        return Response(serializer.data)

    def put(self, request, evaluation_attribute_pk, format=None):
        evaluation_attribute = self.get_object(evaluation_attribute_pk)
        serializer = EvaluationAttributeSerializer(
            evaluation_attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # Partially update a specific entry by primary key
    def patch(self, request, evaluation_attribute_pk):
        evaluation_attribute = self.get_object(evaluation_attribute_pk)
        serializer = EvaluationAttributeSerializer(
            evaluation_attribute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, evaluation_attribute_pk, format=None):
        try:
            evaluation_attribute = self.get_object(evaluation_attribute_pk)
            evaluation_attribute.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            # Handle the error and send a response to the frontend.
            return Response({
                "error": "Cannot delete because Student Reports exist with this attribute. Please contact support for help."
            }, status=400)  # Or appropriate error code, 400 is for Bad Request.
