# Generated by Django 4.2.1 on 2025-02-16 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_delete_textevaluationattribute'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EvaluationAttribute',
        ),
    ]
