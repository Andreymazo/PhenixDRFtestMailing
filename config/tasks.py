from celery import shared_task

from config.celery import app
from mailing.models import Clientt, Mailing

from mailing.service import send


# @app.task
@shared_task
def send_request():
    for i in Clientt.objects.all():

        pass
        recepient = str(i.phone)
        # message =
        # send(user_email)

