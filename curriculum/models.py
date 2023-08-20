from django.db import models

from schools.models import School

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=255) # e.g., "Octopus", "1", "2", ...
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=255)  # e.g., "Phonics", "Spelling", ...
    school = models.ForeignKey(School, related_name='subjects', on_delete=models.CASCADE)

class SubjectLevel(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    curriculum_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table='curriculum_subject_level'

class Unit(models.Model):
    name = models.CharField(max_length=255)  # e.g., "Unit 1", "Basics", ...
    subject_level = models.ForeignKey(SubjectLevel, related_name='units', on_delete=models.CASCADE)
