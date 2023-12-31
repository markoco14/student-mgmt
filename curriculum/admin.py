from django.contrib import admin

# Register your models here.

from curriculum.models import Module, ModuleType, Assessment, AssessmentType
from curriculum.models.level_model import Level
from curriculum.models.subject_level_model import SubjectLevel
from curriculum.models.subject_model import Subject
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(SubjectLevel)
admin.site.register(Module)
admin.site.register(ModuleType)
admin.site.register(Assessment)
admin.site.register(AssessmentType)
