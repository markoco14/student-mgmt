from django.db import models

from schools.models import School
from users.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, db_column='school_id')

    def __str__(self):
        return f"{self.first_name} {self.last_name} (id: {self.id}) in {self.school_id.name} (id: {self.school_id.id})"
    
# class StudentAttendance(models.Model):
#     """
#     The StudentAttendance model is designed to keep track of individual student attendance records.
    
#     Attributes:
#         - student: A foreign key to the student for whom the attendance is being recorded.
#         - date: The date for which attendance is recorded.
#         - attendance_status: An integer field representing the status of attendance. 
#                              Choices are 0 (On Time), 1 (Late), and 2 (Absent).
#         - reason: A text field that provides an explanation if the student is Late or Absent.
#         - staff: A foreign key to the staff who tracked the attendance.
        
#     The 'reason' attribute becomes particularly useful when a student is marked as either Late or Absent,
#     serving as a note or justification for the absence or tardiness. This can be used later for administrative
#     or educational interventions.
    
#     The model employs Django's choices option for the attendance_status to ensure data consistency.
#     """
     
#     ATTENDANCE_CHOICES = [
#         (0, 'On Time')
#         (1, 'Late')
#         (2, 'Absent')
#     ]

#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     date = models.DateField() # To know what day it is
#     status = models.Choices(choices=ATTENDANCE_CHOICES, default=0) # On Time, Late, Absent
#     reason = models.TextField(null=True, blank=True) # A reason should be given if the student is late/absent
#     staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
