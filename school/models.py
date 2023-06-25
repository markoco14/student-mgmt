from django.db import models
from user.models import User

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True, null=False)
    # updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
