# Generated by Django 4.2.1 on 2025-02-17 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_schooluser_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
