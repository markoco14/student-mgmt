from rest_framework import serializers
from students.student_serializers import StudentSerializer
from students.models import Student
from reports.models import Report, ReportDetails



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

