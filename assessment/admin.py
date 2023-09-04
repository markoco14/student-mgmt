from django.contrib import admin

from assessment.models.assessment_model import Assessment, AssessmentType


# Register your models here.
admin.site.register(Assessment)
admin.site.register(AssessmentType)