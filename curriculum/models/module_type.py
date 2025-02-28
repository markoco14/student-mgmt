from django.db import models

from schools.models import School


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