from rest_framework import serializers
from curriculum.models.level import Level
from curriculum.models.module import Module
from curriculum.models.module_type import ModuleType
from curriculum.models.subject import Subject
from schools.models import School

class LevelSerializer(serializers.ModelSerializer):
    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())
    class Meta:
        model = Level
        fields = ['id', 'name', 'schoolID', 'order']
        
class SubjectSerializer(serializers.ModelSerializer):
    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())
    class Meta:
        model = Subject
        fields = ['id', 'name', 'schoolID']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = '__all__'