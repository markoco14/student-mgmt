from django.contrib import admin
from evaluation.models.evaluation_data_type_model import EvaluationDataType
from evaluation.models.evaluation_attribute_model import TextEvaluationAttribute, RangeEvaluationAttribute, EvaluationAttribute
from evaluation.models.student_evaluation_model import StudentEvaluation

# Register your models here.
admin.site.register(EvaluationDataType)
admin.site.register(TextEvaluationAttribute)
admin.site.register(RangeEvaluationAttribute)
admin.site.register(EvaluationAttribute)
admin.site.register(StudentEvaluation)
