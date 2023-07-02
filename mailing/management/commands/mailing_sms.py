from django.core.management import BaseCommand

from mailing.models import Mailing, Clientt
from mailing.service import send_request, send


def send_sms():
    url = '...'
    data1 = {'message': "Sent"}
    data2 = {'message': "No sent"}
    client_lst = []
    index = 1
    for i in Clientt.objects.all():
        client_lst.append((str(i.phone), i.mailing.message))
    for i in client_lst:
        send_request(i[0], i[1])
        index += 1
        if index == len(client_lst):
            send(url, data1)
        send(url, data2)


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_sms()

