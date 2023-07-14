# Generated by Django 4.2.1 on 2023-07-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('students', '0001_initial'),
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdetails',
            name='student_id',
            field=models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='report',
            name='class_id',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='classes.class'),
        ),
        migrations.AlterUniqueTogether(
            name='reportdetails',
            unique_together={('report_id', 'student_id')},
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('class_id', 'date')},
        ),
    ]
