from django.contrib.auth.models import User
from django.core.management import BaseCommand

# from mailing.models import Clientt


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email= 'andreymazo@mail.ru',
            is_superuser=True,
            is_staff=True,
            username='andrey_mazo'

        )
        user.set_password('qwert123asd')
        user.save()
