from django.db import models

from schools.models import School

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=255) # e.g., "Octopus", "1", "2", ...
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1) # 1, 2, 3.. used to keep the units in correct order

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
        unique_together=['subject', 'level']

    

class ModuleType(models.Model):
    name = models.CharField(max_length=255) # e.g., "Unit", "Chapter", "Part", "Section", "Page", "Day"
    school = models.ForeignKey(School, related_name="module_types", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}): {self.name} at ({self.school.id}): {self.school.name}"

    class Meta:
        db_table = 'curriculum_model_type'
        unique_together = ['name', 'school']

class Module(models.Model):
    subject_level = models.ForeignKey(SubjectLevel, related_name='modules', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # e.g., "Past Simple", "History of Egypt", "Africa"
    type = models.ForeignKey(ModuleType, related_name="modules", on_delete=models.PROTECT)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True) # e.g., "Students will learn the basics of Past Simple Tense..."
    order = models.PositiveIntegerField() # 1, 2, 3.. used to keep the modules in correct order
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        type_name = self.type.name if self.type else "No Type"
        return f"({self.id}): {type_name} {self.order} {self.name} in {self.subject_level.subject.name} Level {self.subject_level.level.name}"
    
    class Meta:
        db_table='curriculum_module'
        unique_together = ['name', 'order', 'type', 'subject_level']
        ordering = ['order']


