from django.contrib import admin
from .models import Class, ClassStudent, ClassDay

# Register your models here.
admin.site.register(Class)
admin.site.register(ClassDay)
admin.site.register(ClassStudent)