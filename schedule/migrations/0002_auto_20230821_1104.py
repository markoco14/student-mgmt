# Generated by Django 4.2.1 on 2023-08-21 11:04

from django.db import migrations

def populate_weekdays(apps, schema_editor):
    Weekday = apps.get_model('schedule', 'Weekday')
    
    # Hardcoding the choices directly in the migration
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]
    
    for day in days:
        Weekday.objects.get_or_create(day=day) 


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_weekdays),
    ]
