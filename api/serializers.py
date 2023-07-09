from rest_framework import serializers
from classes.models import Class
from students.models import Student
from schools.models import School
from users.models import User
from reports.models import Report

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

    def create(self,validated_data):
        user = User.objects.create(email = validated_data['email'], first_name = validated_data['first_name'], last_name = validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields='__all__'

    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model=Report
        fields='__all__'