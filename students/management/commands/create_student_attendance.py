from django.core.management.base import BaseCommand
from django.utils import timezone
from classes.models import ClassEntity, ClassStudent

from schools.models import SchoolDay
from students.models.student_attendence_model import StudentAttendance
import datetime
import random
import pytz  # Import the pytz library

from users.models import User  # Importing Python's random module


class Command(BaseCommand):
    help = 'Automatically add student attendance records for the current day'

    def handle(self, *args, **options):
        # 1) Get the current date and time
        taipei_tz = pytz.timezone('Asia/Taipei')
        current_date = timezone.now().astimezone(taipei_tz).date() + datetime.timedelta(days=3) 
        # + datetime.timedelta(days=1) # in case you need to add days
        current_day = current_date.strftime('%A')
        print(f"timezone: {taipei_tz}")
        print(f"timezone date: {current_date}")
        print(f"timezone day: {current_day}")

        user = User.objects.get(id=1)

        # 2) Check if the current day is a school day
        if SchoolDay.objects.filter(day__day=current_day).exists():
            print('got some SchoolDay objects')

            # 3) Get all classes scheduled for this day
            class_entities = ClassEntity.objects.filter(days__day__day=current_day)
            if class_entities.exists():
                for class_entity in class_entities:
                    # 4) Get the list of students in each class
                    class_students = ClassStudent.objects.filter(
                        class_id=class_entity.id)

                    # 5) Loop through each student and create an attendance record
                    for class_student in class_students:
                        StudentAttendance.objects.create(
                            student_id=class_student.student_id,
                            date=current_date,
                            status=0,  # default to 'On Time'
                            author_id=None  # substitute with a default user
                        )
                        print(f"success for {class_student.student_id.first_name}")
        else:
            print('It is not a school day. Skipping for now.')

        self.stdout.write(self.style.SUCCESS(
            'Successfully recorded attendance'))
