from django.core.management import BaseCommand

from mailing.models import Clientt, Mailing


def send_request1():# Рассылка 1 №№№№№№№№№№№
    recepient_lst = []
    message = Mailing.objects.all().get(pk=1).message
    for i in Clientt.objects.all():
        recepient_lst.append((i.phone, message))
    # print(recepient_lst)
    # return recepient_lst
    for i in recepient_lst:
        print((str(i[0]), i[1]))


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_request1()
