from rest_framework import serializers
from schools.models import School, SchoolAccessPermission, SchoolDay, SchoolUser
from users.models import Teacher

class SchoolAccessPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAccessPermission
        fields = ['role_id', 'user_id', 'school_id']

class SchoolDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']

class SchoolDayListSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField()

    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']
        
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






