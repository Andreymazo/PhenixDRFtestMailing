
from django.core.management import BaseCommand

from mailing.models import Mailing, Clientt
from mailing.service import send_request


def send_sms():
    for i in Clientt.objects.all():

        send_request(i.phone, i.mailing.message)

        # print(i.phone)
        # print(i.mailing.message)


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_sms()

        # phone = '+79219507392',
        # user = Client.objects.create(
        #     email= 'andreymazo@mail.ru',
        #     is_superuser=True,
        #     is_staff=True,
        #     phone='+79219507392',
        #     country_phone_code = f'{phone}'[2:4],
        # )
        # user.set_password('qwert123asd')
        # user.save()
