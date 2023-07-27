from django.db import models
from users.models import Teacher, User

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='owner_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SchoolUser(models.Model):
    school = models.ForeignKey(School, db_column='school', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, db_column='user', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schools_school_users'
        unique_together = ['school_id', 'user_id']
        verbose_name_plural = 'School users'