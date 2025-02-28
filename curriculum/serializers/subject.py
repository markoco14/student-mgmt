from rest_framework import serializers
from curriculum.models.level import Level
from curriculum.models.module import Module
from curriculum.models.module_type import ModuleType
from curriculum.models.subject import Subject
from schools.models import School


        
class SubjectSerializer(serializers.ModelSerializer):
    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())
    class Meta:
        model = Subject
        fields = ['id', 'name', 'schoolID']
