from django.core.management.base import BaseCommand

from curriculum.models import Level, Subject, SubjectLevel

class Command(BaseCommand):
    help = 'Create SubjectLevel connections'

    def handle(self, *args, **kwargs):
        try:
            phonics_subject = Subject.objects.get(name='Phonics')
            reading_subject = Subject.objects.get(name='Reading')
            grammar_subject = Subject.objects.get(name='Grammar')

            # Connect Phonics with levels 1-4
            for level_num in range(1, 5):
                level = Level.objects.get(name=str(level_num))
                SubjectLevel.objects.get_or_create(subject=phonics_subject, level=level)

            # Connect Reading and Grammar with levels 5-12
            for level_num in range(5, 13):
                level = Level.objects.get(name=str(level_num))
                SubjectLevel.objects.get_or_create(subject=reading_subject, level=level)
                SubjectLevel.objects.get_or_create(subject=grammar_subject, level=level)

            self.stdout.write(self.style.SUCCESS(f'Successfully created SubjectLevel connections'))

        except (Subject.DoesNotExist, Level.DoesNotExist):
            self.stdout.write(self.style.ERROR('One or more Subjects or Levels do not exist.'))
