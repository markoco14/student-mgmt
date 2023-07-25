# Generated by Django 4.2.1 on 2023-07-25 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
        ('classes', '0005_alter_class_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='level',
            field=models.ForeignKey(db_column='level', default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='classes', to='levels.level'),
        ),
    ]
