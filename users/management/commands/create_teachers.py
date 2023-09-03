from django.core.management.base import BaseCommand
from users.models import Teacher, User  # Replace 'users' with the name of the app where your User model resides
from faker import Faker

class Command(BaseCommand):
    help = 'Create fake teachers'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        for _ in range(5):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()

            user = Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_active=True,
            )
            user.set_password("passtheball1")  # You can set a default password or generate one
            user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 5 teachers'))
