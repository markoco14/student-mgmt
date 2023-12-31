# Generated by Django 4.2.1 on 2023-09-03 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_schoolday'),
        ('curriculum', '0008_alter_module_subject_level_assessmenttype_assessment'),
        ('classes', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='day',
        ),
        migrations.AlterField(
            model_name='class',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='classes', to='curriculum.level'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ClassDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
                ('school_day_id', models.ForeignKey(db_column='school_day_id', on_delete=django.db.models.deletion.CASCADE, to='schools.schoolday')),
            ],
            options={
                'verbose_name_plural': 'Class days',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='days',
            field=models.ManyToManyField(related_name='classes', through='classes.ClassDay', to='schools.schoolday'),
        ),
    ]
