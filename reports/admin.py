from django.contrib import admin

from reports.models import Report, ReportDetails

# Register your models here.
admin.site.register(Report)
admin.site.register(ReportDetails)
