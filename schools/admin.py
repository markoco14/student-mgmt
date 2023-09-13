from django.contrib import admin
from .models import School, SchoolUser, SchoolDay, Role, SchoolAccessPermission

# Register your models here.
admin.site.register(School)
admin.site.register(SchoolUser)
admin.site.register(SchoolDay)
admin.site.register(Role)
admin.site.register(SchoolAccessPermission)
