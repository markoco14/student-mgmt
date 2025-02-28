from rest_framework import serializers

from curriculum.models.level import Level
from schools.models import School

class LevelSerializer(serializers.ModelSerializer):
    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())
    class Meta:
        model = Level
        fields = ['id', 'name', 'schoolID', 'order']