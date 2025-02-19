from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework import serializers

from users.models import Admin, Teacher, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], membership=validated_data['membership'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id', 'email', 'membership']

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user = Teacher.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user = Admin.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user




