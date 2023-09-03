from django.contrib import admin
from .models import ClassEntity, ClassStudent, ClassDay

# Register your models here.
admin.site.register(ClassEntity)
admin.site.register(ClassDay)
admin.site.register(ClassStudent)