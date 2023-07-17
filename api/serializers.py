from rest_framework import serializers
from classes.models import Class, ClassStudent
from levels.models import Level
from students.models import Student
from schools.models import School
from users.models import User
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


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class_list = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = '__all__'

    def get_class_list(self, obj):
        print(obj)
        class_list = ClassStudent.objects.filter(class_id=obj.id)
        serializer = ClassStudentSerializer(class_list, many=True)

        return serializer.data


class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'


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
        print('printing obj', obj.student_id.id)
        student = Student.objects.get(id=obj.student_id.id)
        serializer = StudentSerializer(student, many=False)
        return serializer.data


class LevelSerializser(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
