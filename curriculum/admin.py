from django.contrib import admin

# Register your models here.

from curriculum.models import Module, ModuleType
from curriculum.models.level import Level
from curriculum.models.course import SubjectLevel
from curriculum.models.subject import Subject
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(SubjectLevel)
admin.site.register(Module)
admin.site.register(ModuleType)
# admin.site.register(Assessment)
