from django.db import models
from users.models import User

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='owner_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
