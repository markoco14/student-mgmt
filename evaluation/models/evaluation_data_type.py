from django.db import models

class EvaluationDataType(models.Model):
    """
    The EvaluationDataType model is designed to restrict the types of data that schools can use for student evaluations.
    The available types are:
    - 0: String
    - 1: Boolean
    - 2: Number
    """


    TYPE_CHOICES = [
		(0, 'String'),
		(1, 'Boolean'),
		(2, 'Number'),
    ]

    data_type = models.IntegerField(choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_data_type_display()}"

    class Meta:
        db_table = 'evaluation_evaluation_data_types'
