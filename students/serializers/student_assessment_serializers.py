from rest_framework import serializers
from api.serializers.serializers import StudentSerializer
from assessment.serializers.assessment_serializer import AssessmentSerializer
from students.models.student_assessment_model import StudentAssessment

class StudentAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssessment
        fields = '__all__'

class StudentAssessmentDetailSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer(source='assessment_id')

    class Meta:
        model = StudentAssessment
        fields = '__all__'


# class StudentAssessmentWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentAssessment
#         fields = '__all__'
