from rest_framework import serializers
from student.models import Student
from school.models import School
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'