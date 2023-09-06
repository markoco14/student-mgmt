from django.core.management.base import BaseCommand
from evaluation.models import EvaluationDataType

class Command(BaseCommand):
    help = 'Populates EvaluationDataType table with default types.'

    def handle(self, *args, **options):
        # Check if the table is empty
        if EvaluationDataType.objects.count() == 0:
            # Create the default data types
            types = [
                (0, 'Text'),
                (1, 'Range'),
            ]
            
            for type_id, type_name in types:
                EvaluationDataType.objects.create(data_type=type_id)
                self.stdout.write(self.style.SUCCESS(f'Successfully created data type {type_name}'))
        
        else:
            self.stdout.write(self.style.SUCCESS('EvaluationDataType table already populated.'))
