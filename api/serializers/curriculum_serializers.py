from rest_framework import serializers
from curriculum.models import Level, Subject, SubjectLevel, Unit

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectLevelSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    level = LevelSerializer()
    class Meta:
        model = SubjectLevel
        fields = '__all__'

        
class SubjectLevelWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubjectLevel
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'