# Generated by Django 4.2.1 on 2025-02-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0011_alter_assessment_unique_together_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assessment',
        ),
    ]
