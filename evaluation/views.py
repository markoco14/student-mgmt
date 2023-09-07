from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from evaluation.models.evaluation_attributes import RangeEvaluationAttribute, TextEvaluationAttribute
from evaluation.serializers import RangeEvaluationAttributeSerializer, TextEvaluationAttributeSerializerSerializer

# Create your views here.

@api_view(['GET'])
def get_daily_report_eval_attributes(request, school_pk=None):
    try:
        range_attributes = RangeEvaluationAttribute.objects.filter(school_id=school_pk)
        range_serializer = RangeEvaluationAttributeSerializer(range_attributes, many=True)

        text_attributes = TextEvaluationAttribute.objects.filter(school_id=school_pk)
        text_serializer = TextEvaluationAttributeSerializerSerializer(text_attributes, many=True)

        data = list(range_serializer.data) + list(text_serializer.data)

        return Response(data)
    except RangeEvaluationAttribute.DoesNotExist:
        return Response({"details": "No objects with that School ID found."})