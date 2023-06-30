from django.core.management import BaseCommand

from mailing.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        phone = '+79219507392',
        user = Client.objects.create(
            email= 'andreymazo@mail.ru',
            is_superuser=True,
            is_staff=True,
            phone='+79219507392',
            country_phone_code = f'{phone}'[2:4],
        )
        user.set_password('qwert123asd')
        user.save()
