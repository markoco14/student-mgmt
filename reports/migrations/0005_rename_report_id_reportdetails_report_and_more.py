# Generated by Django 4.2.1 on 2023-08-16 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('reports', '0004_rename_content_reportdetails_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportdetails',
            old_name='report_id',
            new_name='report',
        ),
        migrations.RenameField(
            model_name='reportdetails',
            old_name='student_id',
            new_name='student',
        ),
        migrations.AlterUniqueTogether(
            name='reportdetails',
            unique_together={('report', 'student')},
        ),
    ]