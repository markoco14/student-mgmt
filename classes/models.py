from django.db import models
from schedule.models import Weekday
from curriculum.models import Level

from schools.models import School, SchoolDay
from students.models import Student
from users.models import User

# Create your models here.


class ClassEntity(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name="classes", on_delete=models.PROTECT)
    days = models.ManyToManyField(SchoolDay, through='ClassDay', related_name="classes")
    teacher = models.ForeignKey(User, related_name="classes", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (id: {self.id}) in {self.school.name} (id: {self.school.id})"
    
    class Meta:
        db_table = 'classes_class_entities'
        verbose_name_plural = 'Class entities'

class ClassDay(models.Model):
    class_id = models.ForeignKey(ClassEntity, db_column='class_id', on_delete=models.CASCADE)
    school_day_id = models.ForeignKey(SchoolDay, db_column='school_day_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.class_id.name} on {self.school_day_id.day.day}"
    
    class Meta:
        db_table = 'classes_class_days'
        verbose_name_plural = 'Class days'

class ClassStudent(models.Model):
    class_id = models.ForeignKey(
        ClassEntity, db_column='class_id', on_delete=models.CASCADE)
    student_id = models.ForeignKey(
        Student, db_column='student_id', related_name='class_students', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id.first_name} {self.student_id.last_name} (id: {self.student_id.id}) in {self.class_id.name} (id: {self.class_id.id}) in {self.class_id.school.name}: (id: {self.class_id.school.id})"

    class Meta:
        db_table = 'classes_class_students'
        unique_together = ['class_id', 'student_id']

        
