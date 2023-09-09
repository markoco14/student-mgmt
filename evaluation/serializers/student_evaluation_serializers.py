from rest_framework import serializers
from api.serializers.serializers import StudentSerializer

from evaluation.models.student_evaluations import StudentEvaluation
from evaluation.serializers.evaluation_attribute_serializers import EvaluationAttributeSerializer



class StudentEvaluationSerializer(serializers.ModelSerializer):
    evaluation_attribute = EvaluationAttributeSerializer(source="evaluation_attribute_id")
    student = StudentSerializer(source="student_id")
    class Meta:
        model = StudentEvaluation
        fields = '__all__'
        
				

