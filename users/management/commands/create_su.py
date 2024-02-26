from django.core.management import BaseCommand
from users.models import User
from config.settings import ADMIN_PASS


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='musernik@gmail.com',
            first_name='admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True,
            )

        user.set_password(ADMIN_PASS)
        user.save()
