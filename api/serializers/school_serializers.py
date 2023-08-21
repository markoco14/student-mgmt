from rest_framework import serializers
from schools.models import SchoolDay

class SchoolDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolDay
        fields = '__all__'