# Generated by Django 4.2.1 on 2023-08-21 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='classstudent',
            unique_together={('class_id', 'student_id')},
        ),
    ]
