from django.core.management.base import BaseCommand
from assessment.models.assessment_model import AssessmentType

class Command(BaseCommand):
    help = 'Creates initial Assessment Types'

    def handle(self, *args, **options):
        # Creating 'Homework' AssessmentType
        homework, created = AssessmentType.objects.get_or_create(
            name='Homework'
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Homework AssessmentType'))
        else:
            self.stdout.write(self.style.SUCCESS('Homework AssessmentType already exists'))

        # Creating 'Test' AssessmentType
        test, created = AssessmentType.objects.get_or_create(
            name='Test'
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Test AssessmentType'))
        else:
            self.stdout.write(self.style.SUCCESS('Test AssessmentType already exists'))
