from django.db import models

from schools.models import School

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)