from rest_framework import serializers
from students.serializers.serializers import StudentSerializer
from students.models.student import Student
from students.models.student_attendence_model import StudentAttendance


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'


class StudentWithAttendanceSerializer(serializers.ModelSerializer):
    attendance_for_day = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = "__all__"
        
    def get_attendance_for_day(self, object):
        class_id = self.context.get('class_entity')
        date =  self.context.get('date')

        if class_id and date:
            attendance = object.attendance.filter(date=date, class_id=class_id).first()
            if attendance:
                return StudentAttendanceSerializer(attendance).data
        
        return None
		


class StudentAttendanceDetailSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='student_id')

    class Meta:
        model = StudentAttendance
        fields = '__all__'


class StudentAttendanceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'
