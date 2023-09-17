from rest_framework import serializers

from evaluation.models.evaluation_attribute_model import RangeEvaluationAttribute


class RangeEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangeEvaluationAttribute
        fields = '__all__'
