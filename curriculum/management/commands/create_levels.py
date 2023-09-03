from django.core.management.base import BaseCommand
from curriculum.models import Level

from schools.models import School

class Command(BaseCommand):
    help = 'Create levels 1-15 for the school with id=1'

    def handle(self, *args, **kwargs):
        try:
            school = School.objects.get(pk=1)
        except School.DoesNotExist:
            self.stdout.write(self.style.ERROR('School with id=1 does not exist.'))
            return

        for i in range(1, 16):  # Loops from 1 to 15
            level, created = Level.objects.get_or_create(
                name=str(i),
                order=i,
                school=school,
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Level {i}'))
            else:
                self.stdout.write(self.style.WARNING(f'Level {i} already exists'))

