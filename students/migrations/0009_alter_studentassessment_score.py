# Generated by Django 4.2.1 on 2023-09-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_studentassessment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassessment',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]