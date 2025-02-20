"""
all school related models
"""
import uuid

from django.db import models
from django.utils.text import slugify
from schedule.models import Weekday
from users.models import User

# Create your models here.


class School(models.Model):
    """
    School model
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_column='owner_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (id: {self.id}) Owner: {self.owner_id.first_name} {self.owner_id.last_name} (id: {self.owner_id.id})"


class SchoolUser(models.Model):
    """
    School user model, who has access to what schools
    """

    # Role Choices
    ROLE_OWNER = "owner"
    ROLE_ADMIN = "admin"
    ROLE_TEACHER = "teacher"

    ROLE_CHOICES = [
        (ROLE_OWNER, "OWNER"),
        (ROLE_ADMIN, "ADMIN"),
        (ROLE_TEACHER, "TEACHER"),
    ]

    school = models.ForeignKey(School, db_column='school', related_name='school_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_column='user', related_name='schools', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_TEACHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schools_school_users'
        unique_together = ['school', 'user']
        verbose_name_plural = 'School users'
    
    def __str__(self):
        return f"{self.user.first_name} (id: {self.user.id}) can access {self.school.name} (id: {self.school.id})"
    
    

class Role(models.Model):
    """
    Role model, what roles are available at schools
    """
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class SchoolAccessPermission(models.Model):
    """
    School access permission model, who can access the school and what can they do
    """
    school_id = models.ForeignKey(School, db_column='school_id', related_name="access_permissions", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, db_column="user_id", related_name="access_permissions", on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, db_column="role_id", related_name="access_permissions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name} ({self.user_id.id}) can access {self.school_id.name} as {self.role_id.name}"
    
class SchoolDay(models.Model):
    """
    School day model. what days are the schools open.
    """
    school = models.ForeignKey(School, related_name='days', on_delete=models.CASCADE)

    # Role Choices
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

    DAY_CHOICES = [
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday")
    ]

    # day = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=DAY_CHOICES, default=MONDAY)

    def __str__(self):
        return f"School day (id: {self.id}) @ {self.school.name} (id: {self.school.id})."
    
    class Meta:
        db_table = 'schools_school_days'
        unique_together = ['school', 'day']