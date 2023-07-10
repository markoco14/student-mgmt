from django.db import models

from classes.models import Class

# Create your models here.
class Report(models.Model):
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=150, default="")
    is_complete = models.BooleanField(default=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=['class_id', 'date']