from django.core.management.base import BaseCommand
from django.utils.text import slugify
from schools.models import School
import uuid

class Command(BaseCommand):
    help = "Generate unique slugs for existing schools"

    def handle(self, *args, **kwargs):
        schools = School.objects.filter(slug__isnull=True)
        for school in schools:
            slug = f"{slugify(school.name)}-{uuid.uuid4().hex[:4]}"
            school.slug = slug
            school.save()