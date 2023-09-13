import random
from django.core.management.base import BaseCommand
from classes.models import ClassDay, ClassEntity
from curriculum.models import Level
from schedule.models import Weekday

from schools.models import School, SchoolDay
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Make sure School with id=1 exists
        school_id =input('what is the school id?')
        try:
            school = School.objects.get(pk=school_id)
        except School.DoesNotExist:
            print("School with id=1 does not exist.")
            return
        
        # Get all levels and weekdays for the school
        levels = Level.objects.filter(school=school)
        available_days = SchoolDay.objects.filter(school=school)
        print('available week days',available_days)

        # return
        if not levels.exists() or not available_days.exists():
            print("Not enough Levels or Available to create classes.")
            return
        # return 
        # Create 10 ClassEntity instances
        for i in range(10):
            level = random.choice(levels)
            # week_day = random.choice(week_days)
            available_day = random.choice(available_days)
            # print(week_day)
            print('chosen day', available_day)
            # return
            print('level', level.order)
            print('weekday', available_day.day)
            # continue
            
            # continue
            teachers = User.objects.filter(role='TEACHER')
            teacher = random.choice(teachers)  # Assuming a User exists
            class_name = f"Level {level.order} - {available_day.day} - Teacher: {teacher.first_name} {teacher.last_name[0]}"
            print ('class name', class_name)

            class_entity = ClassEntity.objects.create(
                name=class_name,
                school=school,
                level=level,
                teacher=teacher,
            )

            # Now create associated ClassDay instances
            ClassDay.objects.create(
                class_id=class_entity,
                school_day_id=available_day,
            )

            print(f"Created class {class_name}")
