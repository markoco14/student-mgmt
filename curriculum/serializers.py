from rest_framework import serializers
from curriculum.models import Level, Module, Subject, SubjectLevel

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

class SubjectLevelListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    level = LevelSerializer()
    class Meta:
        model = SubjectLevel
        fields = '__all__'

        
class SubjectLevelWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubjectLevel
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'