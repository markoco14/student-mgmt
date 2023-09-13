from rest_framework import serializers
from schools.models import SchoolAccessPermission, SchoolDay


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






