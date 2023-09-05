# Generated by Django 4.2.1 on 2023-09-04 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
        ('students', '0006_studentassessment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentassessment',
            unique_together={('student_id', 'assessment_id')},
        ),
        migrations.AlterModelTable(
            name='studentassessment',
            table='students_student_assessments',
        ),
    ]
