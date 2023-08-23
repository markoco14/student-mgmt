from rest_framework import serializers
from curriculum.models import Level, Subject, SubjectLevel

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectLevel
        fields = '__all__'