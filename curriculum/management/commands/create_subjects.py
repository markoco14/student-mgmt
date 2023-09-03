from django.core.management.base import BaseCommand
from curriculum.models import Subject

from schools.models import School

class Command(BaseCommand):
    help = 'Create subjects: Phonics, Reading, and Grammar for the school with id=1'

    def handle(self, *args, **kwargs):
        try:
            school = School.objects.get(pk=1)
        except School.DoesNotExist:
            self.stdout.write(self.style.ERROR('School with id=1 does not exist.'))
            return

        subjects_to_create = ['Phonics', 'Reading', 'Grammar']

        for subject_name in subjects_to_create:
            subject, created = Subject.objects.get_or_create(
                name=subject_name,
                school=school,
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Subject: {subject_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Subject {subject_name} already exists.'))

