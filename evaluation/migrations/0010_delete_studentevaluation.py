# Generated by Django 4.2.1 on 2025-02-16 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_alter_studentevaluation_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentEvaluation',
        ),
    ]
