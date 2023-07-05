from rest_framework import serializers
from student.models import Student
from school.models import School
from user.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

    def create(self,validated_data):
        user = CustomUser.objects.create(email = validated_data['email'], first_name = validated_data['first_name'], last_name = validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'