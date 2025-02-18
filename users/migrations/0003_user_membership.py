# Generated by Django 4.2.1 on 2025-02-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='membership',
            field=models.CharField(choices=[('OWNER', 'Owner'), ('STAFF', 'Staff')], default='STAFF', max_length=10),
        ),
    ]
