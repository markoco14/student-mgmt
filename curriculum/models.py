from django.db import models

from schools.models import School

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=255) # e.g., "Octopus", "1", "2", ...
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)

    def __str__(self):
        return f"Level {self.name} in {self.school.name} ({self.id})"

class Subject(models.Model):
    name = models.CharField(max_length=255)  # e.g., "Phonics", "Spelling", ...
    school = models.ForeignKey(School, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.school.name} ({self.id})"

class SubjectLevel(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    curriculum_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject.name} Level {self.level.name} in {self.subject.school.name}"
    class Meta:
        db_table='curriculum_subject_level'

    
class Unit(models.Model):
    subject_level = models.ForeignKey(SubjectLevel, related_name='units', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # e.g., "Unit 1", "Basics", ...
    description = models.TextField(blank=True, null=True) # e.g., "Students will learn the basics of Past Simple Tense..."
    order = models.PositiveIntegerField() # 1, 2, 3.. used to keep the units in correct order

    def __str__(self):
        return f"Unit {self.order}: {self.name} ({self.id}) in {self.subject_level.subject.name} Level {self.subject_level.level.name}"
    
    class Meta:
        db_table='curriculum_unit'
