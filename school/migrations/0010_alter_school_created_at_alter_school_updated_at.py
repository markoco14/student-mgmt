# Generated by Django 4.2.1 on 2023-06-25 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_school_created_at_alter_school_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 10, 9, 43, 179772)),
        ),
        migrations.AlterField(
            model_name='school',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 10, 9, 43, 179786)),
        ),
    ]
