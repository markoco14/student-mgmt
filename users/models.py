from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    MEMBERSHIP_OWNER = "OWNER"
    MEMBERSHIP_STAFF = "STAFF"

    # (Variable name, Readable value)
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_OWNER, "Owner"),
        (MEMBERSHIP_STAFF, "Staff")
    ]

    membership = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_STAFF)

    def __str__(self):
        return f"User: {self.id} - Name: {self.first_name} {self.last_name} - Email: {self.email}"

class OwnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.OWNER)
    
class Owner(User):
    base_membership = User.MEMBERSHIP_OWNER
    objects = OwnerManager()

    class Meta:
        proxy = True

class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.TEACHER)

class Teacher(User):
    base_membership = User.MEMBERSHIP_STAFF
    objects = TeacherManager()

    class Meta:
        proxy = True
        

class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.ADMIN)

class Admin(User):
    base_membership = User.MEMBERSHIP_STAFF
    objects = AdminManager()

    class Meta:
        proxy = True



