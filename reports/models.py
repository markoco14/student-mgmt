from django.db import models

from students.models import Student

# Create your models here.
class Report(models.Model):
    content = models.TextField(max_length=150, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id', unique_for_date='created_at')
    is_complete = models.BooleanField(default=False)