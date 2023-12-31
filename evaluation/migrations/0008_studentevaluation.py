# Generated by Django 4.2.1 on 2023-09-07 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0008_alter_module_subject_level_assessmenttype_assessment'),
        ('students', '0009_alter_studentassessment_score'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0010_remove_classassessment_date_due_and_more'),
        ('evaluation', '0007_evaluationattribute_rangeevaluationattribute_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_type', models.IntegerField(choices=[(0, 'Daily')], default=0)),
                ('date', models.DateField()),
                ('evaluation_value', models.TextField(blank=True, null=True)),
                ('author_id', models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.PROTECT, related_name='written_student_evaluations', to=settings.AUTH_USER_MODEL)),
                ('class_id', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.PROTECT, related_name='evaluations', to='classes.classentity')),
                ('evaluation_attribute_id', models.ForeignKey(blank=True, db_column='evaluation_attribute_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_evaluations', to='evaluation.evaluationattribute')),
                ('level_id', models.ForeignKey(db_column='level_id', on_delete=django.db.models.deletion.PROTECT, related_name='evaluations', to='curriculum.level')),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.PROTECT, related_name='evaluations', to='students.student')),
                ('subject_id', models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.PROTECT, related_name='evaluations', to='curriculum.subject')),
            ],
            options={
                'db_table': 'evaluation_student_evaluations',
                'unique_together': {('student_id', 'date', 'class_id')},
            },
        ),
    ]
