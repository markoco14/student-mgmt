from django.db import models

from schools.models import School
from students.models import Student

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=50)
    school_id = models.ForeignKey(
        School, db_column='school_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClassStudent(models.Model):
    class_id = models.ForeignKey(
        Class, db_column='class_id', on_delete=models.CASCADE)
    student_id = models.ForeignKey(
        Student, db_column='student_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'classes_class_students'
        unique_together = ['class_id', 'student_id']
        
