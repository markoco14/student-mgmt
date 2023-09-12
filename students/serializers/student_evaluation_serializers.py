from rest_framework import serializers
from api.serializers.serializers import StudentSerializer
from evaluation.serializers.student_evaluation_serializers import StudentEvaluationSerializer
from students.models.student import Student
from students.models.student_attendence_model import StudentAttendance


class StudentWithEvaluationSerializer(serializers.ModelSerializer):
    evaluations_for_day = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = "__all__"
        
    def get_evaluations_for_day(self, object):
        class_id = self.context.get('class_entity')
        date =  self.context.get('date')

        if class_id and date:
            evaluations = object.evaluations.filter(date=date, class_id=class_id)
            if evaluations:
                return StudentEvaluationSerializer(evaluations, many=True).data
        
        return None
		