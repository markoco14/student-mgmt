from django.contrib import admin
from .models import ClassEntity, ClassStudent, ClassDay, ClassAssessment

# Register your models here.
admin.site.register(ClassEntity)
admin.site.register(ClassDay)
admin.site.register(ClassStudent)
admin.site.register(ClassAssessment)