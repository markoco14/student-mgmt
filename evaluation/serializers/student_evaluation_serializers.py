from rest_framework import serializers
from api.serializers.serializers import StudentSerializer

from evaluation.models.student_evaluation_model import StudentEvaluation
from evaluation.serializers.evaluation_attribute_serializers import EvaluationAttributeSerializer


class StudentEvaluationSerializer(serializers.ModelSerializer):
    evaluation_attribute = EvaluationAttributeSerializer(
        source="evaluation_attribute_id")

    class Meta:
        model = StudentEvaluation
        fields = '__all__'


class StudentEvaluationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEvaluation
        fields = '__all__'
