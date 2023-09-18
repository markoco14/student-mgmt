from rest_framework import serializers

from evaluation.models.evaluation_data_type_model import EvaluationDataType

class EvaluationDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationDataType
        fields = '__all__'

