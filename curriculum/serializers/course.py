from rest_framework import serializers
from curriculum.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
