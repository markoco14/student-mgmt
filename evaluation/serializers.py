from rest_framework import serializers

from evaluation.models.evaluation_attributes import EvaluationAttribute, RangeEvaluationAttribute, TextEvaluationAttribute


class RangeEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangeEvaluationAttribute
        fields = '__all__'
        
				
class TextEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEvaluationAttribute
        fields = '__all__'


class EvaluationAttributeSerializer(serializers.ModelSerializer):
    rangeevaluationattribute = RangeEvaluationAttributeSerializer(required=False) # Notice the nested serializers
    textevaluationattribute = TextEvaluationAttributeSerializer(required=False)
    class Meta:
        model = EvaluationAttribute
        fields = '__all__'
