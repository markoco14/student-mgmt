# Generated by Django 4.2.1 on 2025-02-28 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0013_alter_subjectlevel_table'),
    ]

    operations = [
        migrations.RenameModel(
           old_name="SubjectLevel",
           new_name="Course"
        ),
        migrations.AlterField(
            model_name='module',
            name='subject_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modules', to='curriculum.course'),
        ),
    ]
