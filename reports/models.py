from django.db import models

from classes.models import Class
from students.models import Student

# Create your models here.
class Report(models.Model):
    date = models.DateField()
    is_complete = models.BooleanField(default=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, db_column='class_id', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=['class_id', 'date']

class ReportDetails(models.Model):
    report = models.ForeignKey(Report, db_column='report_id', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, db_column='student_id', on_delete=models.CASCADE)
    details = models.JSONField(blank=True, default=dict)  # Using a callable default to ensure a new dictionary is created for each instance
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="reports_report_details"
        unique_together = ['report', 'student']
        verbose_name_plural = 'Report details'