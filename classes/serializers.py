from rest_framework import serializers
from schools.models import School
from students.serializers.serializers import StudentSerializer
from classes.models import ClassAssessment, ClassDay, ClassEntity, ClassStudent


class ClassEntitySerializer(serializers.ModelSerializer):
    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())
    class Meta:
        model = ClassEntity
        fields = ['id', 'schoolID', 'name', 'level', 'teacher', 'days']

    # def get_class_list(self, obj):
    #     print(obj)
    #     class_list = ClassStudent.objects.filter(class_id=obj.id)
    #     serializer = ClassStudentSerializer(class_list, many=True)

    #     return serializer.data
    
class ClassEntityWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassEntity
        fields = '__all__'
        
class ClassDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDay
        fields= '__all__'


class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'

class ManageClass_ClassStudentListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='student_id')
    
    class Meta:
        model = ClassStudent
        fields = '__all__'

class ClassAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassAssessment
        fields = '__all__'

class ClassAssessmentDetailSerializer(serializers.ModelSerializer):
    class_entity = ClassEntitySerializer(source='class_id')
    # assessment = AssessmentSerializer(source='assessment_id')

    class Meta:
        model = ClassAssessment
        fields = '__all__'