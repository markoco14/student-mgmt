from rest_framework import serializers
from api.serializers.serializers import StudentSerializer
from students.models.student_attendence_model import StudentAttendance

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

class StudentAttendanceDetailSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='student_id')

    class Meta:
        model = StudentAttendance
        fields = '__all__'


class StudentAttendanceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'
