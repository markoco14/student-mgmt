from rest_framework import serializers
from students.models.student_attendence import StudentAttendance

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'
