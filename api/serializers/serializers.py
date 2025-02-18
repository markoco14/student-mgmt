from rest_framework import serializers
from students.models import Student
from schools.models import School, SchoolUser
from users.models import Admin, Teacher, User
from reports.models import Report, ReportDetails


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





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'


class ReportDetailsSerializer(serializers.ModelSerializer):
    student_info = serializers.SerializerMethodField()

    class Meta:
        model = ReportDetails
        fields = '__all__'

    def get_student_info(self, obj):
        student = Student.objects.get(id=obj.student_id)
        serializer = StudentSerializer(student, many=False)
        return serializer.data

