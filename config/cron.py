from mailing.models import Clientt
from mailing.service import send_request


def send_sms():
    for i in Clientt.objects.all():
        send_request(i.phone, i.mailing.message)
        print(i.phone)
        print(i.mailing.message)


send_sms()
