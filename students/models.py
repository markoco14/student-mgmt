from django.db import models

from schools.models import School

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')

    def __str__(self):
        return f"{self.first_name} {self.last_name} in {self.school_id.name}: ({self.id})"
