from rest_framework import serializers

from evaluation.models.student_evaluations import StudentEvaluation
from evaluation.serializers.evaluation_attribute_serializers import EvaluationAttributeSerializer



class StudentEvaluationSerializer(serializers.ModelSerializer):
    evaluation_attribute = EvaluationAttributeSerializer(source="evaluation_attribute_id")
    class Meta:
        model = StudentEvaluation
        fields = '__all__'
        
				

