from rest_framework import serializers
from classes.models import Class, ClassStudent


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
    
class ClassWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Class
        fields = '__all__'


class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'