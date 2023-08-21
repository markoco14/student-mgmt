# Generated by Django 4.2.1 on 2023-08-21 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_description', models.TextField(blank=True, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.level')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject')),
            ],
            options={
                'db_table': 'curriculum_subject_level',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subject_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='curriculum.subjectlevel')),
            ],
        ),
    ]
