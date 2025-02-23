from django.db import models

from schools.models import School
from users.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])
    photo_url = models.TextField(null=True) # https://storage.googleapis.com/twle-445f4.appspot.com/images/student_4.jpeg student_3 student_2 student_1
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (id: {self.id}) in {self.school.name} (id: {self.school.id})"