from rest_framework import serializers
from curriculum.models import AssessmentType



class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = '__all__'