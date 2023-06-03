from django.db import models

# Create your models here.

class Post(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    title = models.TextField(unique=True)
    slug = models.TextField(null=False)
