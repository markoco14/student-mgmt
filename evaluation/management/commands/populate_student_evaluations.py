import datetime
import random
from django.core.management.base import BaseCommand
from classes.models import ClassEntity, ClassStudent
from evaluation.models.student_evaluations import StudentEvaluation
from curriculum.models import Level, Subject
from students.models.student import Student
from faker import Faker




class Command(BaseCommand):
    help = 'Populates the StudentEvaluation table with dummy data.'

    def handle(self, *args, **options):
        fake = Faker()

        start_time = datetime.datetime.now()

        # Mapping for the subjects based on days
        subjects_by_day = {
            'Monday': 7,
            'Tuesday': 8,
            'Wednesday': 7,
            'Thursday': 10,
            'Friday': 10,
        }

        # Start date
        start_date = datetime.date(2023, 7, 3)  # starting from July 3rd, which is a Monday
        today = datetime.date.today()

        # Loop through all days from the start_date till today
        while start_date <= today:
            day_name = start_date.strftime('%A')  # Get day name like 'Monday', 'Tuesday'...

            if day_name == "Saturday":
                start_date += datetime.timedelta(days=1)
                continue
            
            if day_name == "Sunday":
                start_date += datetime.timedelta(days=1)
                continue

            # Get relevant subject id for the day
            subject_id = subjects_by_day.get(day_name)

            if not subject_id:
                start_date += datetime.timedelta(days=1)  # move to the next day
                continue

            # Fetch classes for the day
            classes_for_day = ClassEntity.objects.filter(days__day__day=day_name)
            for class_entity in classes_for_day:

                # Get students in the class
                # students_in_class = class_entity.class_list.all()
                students_in_class = ClassStudent.objects.filter(class_id=class_entity.id)

                level = Level.objects.get(id=class_entity.level_id)

                for student in students_in_class:
                    print(student)
                    print(student.student_id.id)
                    # return
                    # Randomly choose an evaluation_attribute_id
                    studentObject = Student.objects.get(id = student.student_id.id)
                    eval_attr_id = random.choice([1, 2, 3])

                    # Determine the evaluation value based on eval_attr_id
                    if eval_attr_id == 3:
                        eval_value = fake.sentence(nb_words=9, variable_nb_words=True)  # Generates a sentence with approximately 6 words. Variable number of words ensures a bit of randomness.
                    else:
                        eval_value = str(random.randint(1, 3))

                    # Create the StudentEvaluation record
                    StudentEvaluation.objects.create(
                        evaluation_type=0,
                        student_id=studentObject,
                        author_id_id=1,
                        date=start_date,
                        evaluation_attribute_id_id=eval_attr_id,
                        evaluation_value=eval_value,
                        class_id=class_entity,
                        subject_id_id=subject_id,
                        level_id=level,
                    )

            start_date += datetime.timedelta(days=1)  # move to the next day

        end_time = datetime.datetime.now()
        self.stdout.write(self.style.SUCCESS(f"start_time = {start_time}"))
        self.stdout.write(self.style.SUCCESS(f"end_time = {end_time}"))
        self.stdout.write(self.style.SUCCESS(f"total_time = {end_time - start_time}"))
        self.stdout.write(self.style.SUCCESS('Successfully populated the StudentEvaluation table!'))
