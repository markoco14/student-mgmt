from django.db import models
from assessment.models.assessment_model import Assessment
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

class ClassAssessment(models.Model):
    """
    The ClassAssessment model is designed to manage the association between an Assessment and a ClassEntity. 
    This allows a teacher to assign a specific assessment to a specific class and set a date for when 
    this assignment will be made known to students.

    Attributes:
        - class_id: A foreign key to the ClassEntity to which the assessment is assigned.
        - assessment_id: A foreign key to the Assessment that is being assigned.

        - created_at: A timestamp indicating when this record was created in the database.
        - updated_at: A timestamp indicating the last time this record was updated.

    The 'created_at' and 'updated_at' fields automatically track when the record is created and updated,
    respectively.

    The model employs Django's PROTECT option for both class_id and assessment_id foreign keys to ensure
    that neither the ClassEntity nor the Assessment can be deleted while they have existing links in 
    the ClassAssessment table.
    """

    class_id = models.ForeignKey(ClassEntity, db_column='class_id', related_name='assessments', on_delete=models.PROTECT)
    assessment_id = models.ForeignKey(Assessment, db_column='assessment_id', related_name='classes', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.class_id.name} (id:{self.class_id.id}) given Assessment {self.assessment_id.id}: {self.assessment_id.name}"

    class Meta:
        db_table = 'classes_class_assessments'


        
