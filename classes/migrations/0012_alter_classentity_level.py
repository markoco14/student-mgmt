# Generated by Django 4.2.1 on 2025-02-17 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0012_delete_assessment'),
        ('classes', '0011_remove_classassessment_assessment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classentity',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='curriculum.level'),
        ),
    ]
