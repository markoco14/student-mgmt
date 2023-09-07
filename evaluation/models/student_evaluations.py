from django.db import models
from classes.models import ClassEntity
from curriculum.models import Level, Subject
from evaluation.models.evaluation_attributes import EvaluationAttribute, RangeEvaluationAttribute, TextEvaluationAttribute

from students.models.student import Student
from users.models import User

class StudentEvaluation(models.Model):
    """
    The StudentEvaluation model is designed to keep track of qualitative student evaluations. Such things
    teacher comments, participation, attitude, and other attributes schools will want to track.
    
    Attributes:
        - evaluation_type:
        - student_id: a foreign key to which student
        - author_id: a foreign key to which author
        - date: a record of what day the report happened on
        - evaluation_attribute_id: a foreign key to which evaluation attribute the evaluation belongs to
        - evaluation_value: the value of the evaluation stored as text. will require validations in/out of DB
        - class_id: a foreign key to which class
        - subject_id: a foreign key to which subject
        - level_id: a foreign key to which level
        

    
    The model employs Django's choices option for the evaluation_type to ensure data consistency.
    """

    TYPE_CHOICES = [
        (0, "Daily")
    ]

    evaluation_type = models.IntegerField(choices=TYPE_CHOICES, default=0) # only 1 type for now, but more to come
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="evaluations", db_column="student_id")
    author_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='written_student_evaluations', db_column='author_id')
    date = models.DateField()
    evaluation_attribute_id = models.ForeignKey(EvaluationAttribute, null=True, blank=True, on_delete=models.PROTECT, related_name="student_evaluations", db_column='evaluation_attribute_id')
    evaluation_value = models.TextField(null=True, blank=True) # requires validation for formatting when retrieved from DB
    class_id = models.ForeignKey(ClassEntity, on_delete=models.PROTECT, related_name="evaluations", db_column="class_id")
    subject_id = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="evaluations", db_column="subject_id")
    level_id = models.ForeignKey(Level, on_delete=models.PROTECT, related_name="evaluations", db_column="level_id")

    def __str__(self):
        return f"{self.get_evaluation_type_display()} Evaluation {self.student_id.first_name} {self.date}"

    class Meta:
        unique_together = ['student_id', 'date', 'class_id']
        db_table = 'evaluation_student_evaluations'
