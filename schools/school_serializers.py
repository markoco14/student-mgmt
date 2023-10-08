"""
holds all school related serializers
"""

from rest_framework import serializers
from schools.models import School, SchoolAccessPermission, SchoolDay, SchoolUser
from users.models import Teacher

class SchoolAccessPermissionSerializer(serializers.ModelSerializer):
    """
    serialize school permission data
    """
    class Meta:
        model = SchoolAccessPermission
        fields = ['role_id', 'user_id', 'school_id']

class SchoolDaySerializer(serializers.ModelSerializer):
    """
    serialize school day data ie; what days are schools open
    """
    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']

class SchoolDayListSerializer(serializers.ModelSerializer):
    """
    serialize school day data ie; what days are schools open
    gets the name of the day, not just a number
    """
    day = serializers.StringRelatedField()

    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']
        
class SchoolSerializer(serializers.ModelSerializer):
    """
    serialize school data
    """
    class Meta:
        model = School
        fields = '__all__'

class SchoolUserSerializer(serializers.ModelSerializer):
    """
    serialize school user data, who has access to schools
    """
    # user = serializers.SerializerMethodField()
    
    class Meta:
        model = SchoolUser
        fields = '__all__'
    
    # def get_user(self, obj):
    #     teacher = Teacher.objects.get(id=obj.user.id)
    #     serializer = TeacherSerializer(teacher, many=False)
    #     return serializer.data

class SchoolTeacherSerializer(serializers.ModelSerializer):
    """
    serialize school teacher data, what teachers belong to which schools
    """
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']






