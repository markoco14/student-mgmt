from rest_framework import serializers

from evaluation.models.evaluation_attribute_model import TextEvaluationAttribute
from evaluation.serializers.evaluation_data_type_serializers import EvaluationDataTypeSerializer


class TextEvaluationAttributeSerializer(serializers.ModelSerializer):
    data_type = EvaluationDataTypeSerializer(source='data_type_id', required=False)
        
    class Meta:
        model = TextEvaluationAttribute
        fields = '__all__'
