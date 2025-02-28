from django.db import models

from schools.models import School

class Level(models.Model):
    name = models.CharField(max_length=255) # e.g., "Octopus", "1", "2", ...
    school = models.ForeignKey(School, related_name='levels', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1) # 1, 2, 3.. used to keep the units in correct order

    def __str__(self):
        return f"Level {self.name} in {self.school.name} ({self.id})"