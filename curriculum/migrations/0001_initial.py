# Generated by Django 4.2.1 on 2023-08-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0010_alter_schooluser_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='schools.school')),
            ],
        ),
    ]
