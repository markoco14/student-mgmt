from django.contrib import admin

# Register your models here.

from curriculum.models import Level, Subject, SubjectLevel, Module, ModuleType, Assessment, AssessmentType
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(SubjectLevel)
admin.site.register(Module)
admin.site.register(ModuleType)
admin.site.register(Assessment)
admin.site.register(AssessmentType)
