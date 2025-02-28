from django.db import models
from curriculum.models.course import Course
from curriculum.models.module_type import ModuleType


class Module(models.Model):
    subject_level = models.ForeignKey(Course, related_name='modules', on_delete=models.PROTECT)
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



