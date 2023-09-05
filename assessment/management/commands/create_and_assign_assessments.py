from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from random import choice
import random
from assessment.models.assessment_model import Assessment, AssessmentType

from classes.models import ClassAssessment, ClassEntity
from students.models.student import Student
from students.models.student_assessment_model import StudentAssessment

class Command(BaseCommand):
    help = 'Automatically creates assessments for class entities.'

    def handle(self, *args, **kwargs):
        subjects = ['Grammar', 'Reading']
        levels = list(range(5, 13))  # Level 5 - 12
        units = list(range(1, 6))  # Unit 1 - 5
        homeworks = list(range(1, 3))  # Homework 1 - 2
        tests = list(range(1, 3))  # Test 1 - 2
        scores = [5, 6, 7, 8, 9, 10, 11]

        # Homework Assessment Type ID is 1, Test Assessment Type ID is 2
        assessment_types = {
            'Homework': 1,
            'Test': 2
        }

        class_entities = ClassEntity.objects.all()
        
        for class_entity in class_entities:
            level = class_entity.level.order  # Assuming the level is stored as an integer, use order
            if level not in levels:
                print('level not in levels')
                continue
            print(f"level {level} in levels, continuing")
            # return
            for subject in subjects:
                for unit in units:
                    for homework in homeworks:
                        # Create Homework
                        name = f"{subject} Level {level} Unit {unit} Homework {homework}"
                        date_announced = timezone.now().date()
                        date_due = date_announced + timedelta(days=7)

                        homework_assessment = Assessment.objects.create(
                            name=name,
                            description=f"{name} Description",
                            total_marks=Decimal(random.choice(scores)),
                            date_announced=date_announced,
                            date_due=date_due,
                            assessment_type_id=AssessmentType.objects.get(id=assessment_types['Homework'])
                        )

                        # Create ClassAssessment
                        class_homework = ClassAssessment.objects.create(
                            class_id=class_entity,
                            assessment_id=homework_assessment
                        )

                        # Create StudentAssessment
                        students = Student.objects.filter(class_students__class_id=class_entity)
                        for student in students:
                            StudentAssessment.objects.create(
                                student_id=student,
                                assessment_id=homework_assessment
                            )

                    for test_num in tests:
                        # Create Test
                        name = f"{subject} Level {level} Unit {unit} Test {test_num}"
                        date_written = timezone.now().date()

                        test_assessment = Assessment.objects.create(
                            name=name,
                            description=f"{name} Description",
                            total_marks=Decimal('10.00'),
                            date_announced=date_written,
                            date_due=None,
                            assessment_type_id=AssessmentType.objects.get(id=assessment_types['Test'])
                        )

                        # Create ClassAssessment
                        class_test = ClassAssessment.objects.create(
                            class_id=class_entity,
                            assessment_id=test_assessment
                        )

                        # Create StudentAssessment
                        students = Student.objects.filter(class_students__class_id=class_entity)
                        for student in students:
                            StudentAssessment.objects.create(
                                student_id=student,
                                assessment_id=test_assessment
                            )

        self.stdout.write(self.style.SUCCESS('Successfully created assessments!'))
