from django.core.management.base import BaseCommand
from schools.models import School
from students.models import Student
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Create random students'

    def handle(self, *args, **options):
        fake = Faker()
        
        girl_urls = [
            "https://storage.googleapis.com/twle-445f4.appspot.com/images/student_1.jpeg",
            "https://storage.googleapis.com/twle-445f4.appspot.com/images/student_4.jpeg",
        ]

        boy_urls = [
            "https://storage.googleapis.com/twle-445f4.appspot.com/images/student_2.jpeg",
            "https://storage.googleapis.com/twle-445f4.appspot.com/images/student_3.jpeg",
        ]

        girl_counter = 0
        boy_counter = 0

        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            age = fake.random_int(min=5, max=18, step=1)
            gender = fake.random_element([0, 1])

            if gender == 1:  # Girl
                photo_url = girl_urls[girl_counter % 2]
                girl_counter += 1
            else:  # Boy
                photo_url = boy_urls[boy_counter % 2]
                boy_counter += 1

            # Assuming you have a school object to associate the student with
            school = School.objects.first()  # Or any other logic to get a school object

            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                gender=gender,
                photo_url=photo_url,
                school_id=school,
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 students'))
