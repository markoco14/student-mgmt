from django.db import models
from decimal import Decimal


class AssessmentType(models.Model):
    name = models.CharField(max_length=255) # Homework, Test
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}): {self.name} Assessment"
    class Meta:
        db_table = 'assessment_assessment_types'

class Assessment(models.Model):
    name = models.CharField(max_length=255) # Grammar Level 3 Unit 1 Exercise 1
    description = models.TextField()  # Students will be tested on...
    total_marks = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    date_announced = models.DateField()
    date_due = models.DateField()
    assessment_type_id = models.ForeignKey(AssessmentType, db_column='assessment_type_id', related_name='assessments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}): {self.name}"

    class Meta:
        db_table = 'assessment_assessments'

    

