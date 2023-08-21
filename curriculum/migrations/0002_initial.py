# Generated by Django 4.2.1 on 2023-08-21 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='schools.school'),
        ),
        migrations.AddField(
            model_name='level',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='schools.school'),
        ),
    ]
