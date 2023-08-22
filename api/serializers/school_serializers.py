from rest_framework import serializers
from schools.models import SchoolDay


class SchoolDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']

class SchoolDayListSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField()

    class Meta:
        model = SchoolDay
        fields = ['id', 'school', 'day']






