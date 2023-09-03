from django.core.management.base import BaseCommand
from classes.models import ClassEntity, ClassStudent
from students.models import Student  # Update this import based on where your Student model resides
import itertools

class Command(BaseCommand):
    help = "Automatically adds students to classes"

    def handle(self, *args, **kwargs):
        # Get all available classes
        class_entities = ClassEntity.objects.all()

        # Get all available students
        students = list(Student.objects.all())  # Convert queryset to list for easier manipulation

        if not class_entities.exists() or not students:
            self.stdout.write(self.style.ERROR("Not enough ClassEntities or Students to perform the operation."))
            return

        # Create an iterator that will cycle through the classes indefinitely
        class_cycle = itertools.cycle(class_entities)

        for student in students:
            class_entity = next(class_cycle)

            # Create ClassStudent entry
            ClassStudent.objects.create(
                class_id=class_entity,
                student_id=student,
            )

            self.stdout.write(self.style.SUCCESS(f"Added {student.first_name} {student.last_name} to {class_entity.name}."))
