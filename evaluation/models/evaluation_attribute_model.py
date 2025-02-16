from django.db import models
from evaluation.models.evaluation_data_type_model import EvaluationDataType

from schools.models import School

class EvaluationAttribute(models.Model):
    """
    The EvaluationAttribute model is designed to allow schools to choose what
    qualitative data they want to track for their students. Schools can name their attributes
    with any given name they choose "Participation", "Attitude", "Raises Hand", "Watches Speaker", "Teacher Comment"
    are all acceptable evaluations.

    The main point is the teacher is evaluation the student's performance based on what they observed in the classroom.

    Schools can name the attributes as they see fit. Schools can have as many attributes as they want. But
    they can only choose from data types available in the EvaluationDataType model (a Foreign Key).

    This is an abstraction layer that will use Multi-Table Inheritance
    """
    name = models.CharField(max_length=255)
    school_id = models.ForeignKey(School, db_column='school_id', related_name="evaluation_attributes", on_delete=models.CASCADE)
    data_type_id = models.ForeignKey(EvaluationDataType, db_column="data_type_id", related_name='evaluation_attributes', on_delete=models.PROTECT)

    def __str__(self):
        return f"Evaluation Attribute: {self.name} for School: {self.school_id.name}."

    class Meta:
        db_table = 'evaluation_evaluation_attributes'
        verbose_name_plural = "Evaluation attributes"

