from rest_framework import serializers

from evaluation.models.evaluation_attribute_model import EvaluationAttribute, RangeEvaluationAttribute, TextEvaluationAttribute


class RangeEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangeEvaluationAttribute
        fields = '__all__'


class TextEvaluationAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEvaluationAttribute
        fields = '__all__'


class EvaluationAttributeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationAttribute
        fields = '__all__'


class EvaluationAttributeSerializer(serializers.Serializer):
    rangeevaluationattribute = RangeEvaluationAttributeSerializer(
        required=False)  # Notice the nested serializers
    textevaluationattribute = TextEvaluationAttributeSerializer(required=False)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = super().to_representation(instance)

        # Remove null fields from the representation
        # Return the value of the non-null field directly
        for key, value in ret.items():
            if value is not None:
                return value

        return ret
