from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Create superuser."""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('1')
        user.save()