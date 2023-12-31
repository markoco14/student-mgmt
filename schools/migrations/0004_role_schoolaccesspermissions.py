# Generated by Django 4.2.1 on 2023-09-13 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0003_schoolday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAccessPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, related_name='access_permissions', to='schools.role')),
                ('school_id', models.ForeignKey(db_column='school_id', on_delete=django.db.models.deletion.CASCADE, related_name='access_permissions', to='schools.school')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='access_permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
