from django.contrib import admin

# Register your models here.

from curriculum.models import Level, Subject, SubjectLevel
# Register your models here.
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(SubjectLevel)
