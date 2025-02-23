from rest_framework import serializers
from schools.models import School
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    photoUrl = serializers.CharField(source="photo_url", required=False, allow_null=True, allow_blank=True)

    schoolID = serializers.PrimaryKeyRelatedField(source="school", queryset=School.objects.all())

    class Meta:
        model = Student
        fields = ["id", "firstName", "lastName", "age", "gender", "photoUrl", "schoolID"]
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "photo_url": {"required": False},
        } 
