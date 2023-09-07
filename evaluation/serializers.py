from rest_framework import serializers

from evaluation.models.evaluation_attributes import RangeEvaluationAttribute, TextEvaluationAttribute


class RangeEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangeEvaluationAttribute
        fields = '__all__'
        
				
class TextEvaluationAttributeSerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEvaluationAttribute
        fields = '__all__'

