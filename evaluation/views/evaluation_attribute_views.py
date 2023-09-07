from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from evaluation.models.evaluation_attributes import EvaluationAttribute, RangeEvaluationAttribute, TextEvaluationAttribute
from evaluation.serializers import EvaluationAttributeSerializer, RangeEvaluationAttributeSerializer, TextEvaluationAttributeSerializer

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
    except RangeEvaluationAttribute.DoesNotExist:
        return Response({"details": "No objects with that School ID found."})
