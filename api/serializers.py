from rest_framework import serializers
from student.models import Student
from core.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'