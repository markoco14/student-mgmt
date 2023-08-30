from rest_framework import serializers
from curriculum.models import Assessment, AssessmentType, Module
from curriculum.serializers.curriculum_serializers import ModuleSerializer, SubjectLevelListSerializer, SubjectLevelSerializer





class ModuleAssessmentPageSerializer(serializers.ModelSerializer):
    subject_level = SubjectLevelListSerializer()
    assessments = serializers.SerializerMethodField()

    def get_assessments(self, obj):
        assessments = Assessment.objects.filter(module=obj.id)
        serializer = AssessmentSerializer(assessments, many=True)

        return serializer.data
    
    class Meta:
        model = Module
        fields = '__all__'


class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'