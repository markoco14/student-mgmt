# Generated by Django 4.2.1 on 2023-08-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_alter_schooluser_school'),
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_levels', to='schools.school'),
        ),
    ]