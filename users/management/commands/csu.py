from django.core.management.base import BaseCommand
import os

from dotenv import load_dotenv

from users.models import CustomUser

load_dotenv()

class Command(BaseCommand):

    def handle (self, *args, **kwargs):
        user = CustomUser.objects.create(
            email='admin@mail.com',
            first_name='Admin',
            last_name='User',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('CSU_PASS'))
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Admin user created: {user.email}'))