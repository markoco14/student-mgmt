from django.db import models

from schools.models import School


class Subject(models.Model):
    name = models.CharField(max_length=255)  # e.g., "Phonics", "Spelling", ...
    school = models.ForeignKey(School, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.school.name} ({self.id})"