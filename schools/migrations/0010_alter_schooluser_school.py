# Generated by Django 4.2.1 on 2023-08-19 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_alter_schooluser_school_alter_schooluser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='school',
            field=models.ForeignKey(db_column='school', on_delete=django.db.models.deletion.CASCADE, related_name='school_users', to='schools.school'),
        ),
    ]
