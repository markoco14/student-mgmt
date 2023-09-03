from django.core.management.base import BaseCommand

from schools.models import School, SchoolUser
from users.models import Teacher, User

class Command(BaseCommand):
    help = 'Assign all users to the school with id=1'

    def handle(self, *args, **kwargs):
        try:
            school = School.objects.get(pk=1)
        except School.DoesNotExist:
            self.stdout.write(self.style.ERROR('School with id=1 does not exist.'))
            return

        users = Teacher.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found.'))
            return

        for user in users:
            school_user, created = SchoolUser.objects.get_or_create(
                school=school,
                user=user,
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added User {user.id} to School 1'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user.id} is already added to School 1'))

