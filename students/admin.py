from django.contrib import admin
from .models import Student, StudentAttendance, StudentAssessment


# Register your models here.

admin.site.register(Student)
admin.site.register(StudentAttendance)
admin.site.register(StudentAssessment)