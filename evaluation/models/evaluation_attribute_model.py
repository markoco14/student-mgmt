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

class TextEvaluationAttribute(EvaluationAttribute):
    """
    A model that allows teachers to make a written comment to document student behavior from each class. This could
    be "Teacher's Comment" or "Admin Comment" but it is a written sentence that describes the student's behaviour
    and anything else noteworthy about that student in the class.
    """

    class Meta:
        db_table = "evaluation_text_evaluation_attributes"
        verbose_name_plural = 'Text evaluation attributes'



# class RangeEvaluationAttribute(EvaluationAttribute):
#     """
#     A model that allows teachers to rate student performance numerically. Teachers can choose
#     the scale by which they want to rate students, ie; 1-3, 1-5, 1-7

#     -min_value: the lowest possible value. usually 1.
#     -max_value: the highest possible value. Schools can choose but usually an odd number like 3, 5, 7, 9.
#     -descriptions: an array of descriptions that explain what each number represents
#     """
#     min_value = models.PositiveIntegerField(default=1)
#     max_value = models.PositiveIntegerField()
#     descriptions = models.JSONField(null=True, blank=True) # a description for each numeric value in the range of what it means to the school

#     def save(self, *args, **kwargs):
#         # check the max value is higher than the min value
#         if self.max_value <= self.min_value:
#             raise ValueError(f"max_value ({self.max_value}) must be greater than min_value ({self.min_value})")

        
#         if self.descriptions:
#             expected_count = self.max_value - self.min_value + 1
#             if len(self.descriptions) != expected_count:
#                 raise ValueError(f"Number of descriptions ({len(self.descriptions)}) does not match the range size ({expected_count})")
        
#         super().save(*args, **kwargs)


#     class Meta:
#         db_table = "evaluation_range_evaluation_attributes"
#         verbose_name_plural = 'Range evaluation attributes'
