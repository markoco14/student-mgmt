from rest_framework import serializers

from evaluation.models.student_evaluations import StudentEvaluation



class StudentEvaluationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentEvaluation
        fields = '__all__'
        
				

