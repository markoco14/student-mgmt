# Generated by Django 4.2.1 on 2023-09-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationdatatype',
            name='data_type',
            field=models.IntegerField(choices=[(0, 'String'), (1, 'Range')]),
        ),
    ]
