from rest_framework import serializers

from evaluation.models.evaluation_attribute_model import TextEvaluationAttribute


class TextEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEvaluationAttribute
        fields = '__all__'
