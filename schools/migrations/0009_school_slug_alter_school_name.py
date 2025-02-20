# Generated by Django 4.2.1 on 2025-02-19 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_alter_schoolday_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
