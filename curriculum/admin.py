from django.contrib import admin

from curriculum.models.module import Module
from curriculum.models.module_type import ModuleType
from curriculum.models.level import Level
from curriculum.models.course import Course
from curriculum.models.subject import Subject

admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(ModuleType)
