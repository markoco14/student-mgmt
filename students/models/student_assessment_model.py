from django.db import models
from decimal import Decimal
# from assessment.models.assessment_model import Assessment

from students.models.student import Student

# Create your models here.

class StudentAssessment(models.Model):
    student_id = models.ForeignKey(Student, db_column='student_id', related_name='assessments', on_delete=models.CASCADE) 
    # assessment_id = models.ForeignKey(Assessment, db_column='assessment_id', related_name='students', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.assessment_id} - Score: {self.score}"
    
    class Meta:
        db_table = 'students_student_assessments'
        