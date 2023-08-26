from rest_framework import serializers
from students.models import Student
from schools.models import School, SchoolUser
from users.models import Teacher, User
from reports.models import Report, ReportDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
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


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolUserSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    
    class Meta:
        model = SchoolUser
        fields = '__all__'
    
    # def get_user(self, obj):
    #     teacher = Teacher.objects.get(id=obj.user.id)
    #     serializer = TeacherSerializer(teacher, many=False)
    #     return serializer.data

class SchoolTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']


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

