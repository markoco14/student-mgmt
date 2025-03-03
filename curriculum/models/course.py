# from curriculum.models import Level, Subject
from django.db import models
from curriculum.models.level import Level

from curriculum.models.subject import Subject


class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name="courses", on_delete=models.CASCADE)
    curriculum_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject.name} Level {self.level.name} in {self.subject.school.name}"
    
    class Meta:
        db_table='curriculum_course'
        unique_together=['subject', 'level']