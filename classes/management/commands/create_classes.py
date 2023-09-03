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
        try:
            school = School.objects.get(pk=1)
        except School.DoesNotExist:
            print("School with id=1 does not exist.")
            return
        
        # Get all levels and weekdays for the school
        levels = Level.objects.filter(school=school)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        week_days = Weekday.objects.filter(day__in=days)  # Monday to Friday
        print('available week days',week_days)
        # return

        if not levels.exists() or not week_days.exists():
            print("Not enough Levels or Weekdays to create classes.")
            return
        
        # Create 10 ClassEntity instances
        for i in range(10):
            level = random.choice(levels)
            week_day = random.choice(week_days)
            print('level', level.order)
            print('weekday', week_day.day)
            # continue
            
            class_name = f"Level {level.order} {week_day.day}"
            print ('class name', class_name)
            # continue
            teacher = User.objects.filter(role='TEACHER').first()  # Assuming a User exists

            class_entity = ClassEntity.objects.create(
                name=class_name,
                school=school,
                level=level,
                teacher=teacher,
            )

            # Now create associated ClassDay instances
            school_day = SchoolDay.objects.filter(school=school, day=week_day).get()
            
           
            ClassDay.objects.create(
                class_id=class_entity,
                school_day_id=school_day,
            )

            print(f"Created class {class_name}")
