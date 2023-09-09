from django.contrib import admin
from evaluation.models.evaluation_data_type import EvaluationDataType
from evaluation.models.evaluation_attributes import TextEvaluationAttribute, RangeEvaluationAttribute, EvaluationAttribute
from evaluation.models.student_evaluations import StudentEvaluation

# Register your models here.
admin.site.register(EvaluationDataType)
admin.site.register(TextEvaluationAttribute)
admin.site.register(RangeEvaluationAttribute)
admin.site.register(EvaluationAttribute)
admin.site.register(StudentEvaluation)
