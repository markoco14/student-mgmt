# Generated by Django 4.2.1 on 2023-09-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_classassessment_date_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classassessment',
            name='date_due',
        ),
        migrations.RemoveField(
            model_name='classassessment',
            name='date_of_announcement',
        ),
    ]