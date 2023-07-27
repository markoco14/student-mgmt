from django.db import models
from users.models import Teacher, User

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='owner_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SchoolUser(models.Model):
    school = models.ForeignKey(School, db_column='school', related_name='school_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_column='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schools_school_users'
        unique_together = ['school', 'user']
        verbose_name_plural = 'School users'