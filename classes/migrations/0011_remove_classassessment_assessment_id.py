# Generated by Django 4.2.1 on 2025-02-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0010_remove_classassessment_date_due_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classassessment',
            name='assessment_id',
        ),
    ]
