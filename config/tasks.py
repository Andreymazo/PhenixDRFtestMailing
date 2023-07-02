from celery import shared_task

from config.celery import app
from mailing.models import Clientt, Mailing

from mailing.service import send, send_request


# @app.task
@shared_task
def send_request1():
    url = '...'
    data1 = {'message': "Sent"}
    data2 = {'message': "No sent"}
    recepient_lst = []
    message = Mailing.objects.all().get(pk=1).message
    index = 1
    for i in Clientt.objects.all():
        recepient_lst.append((i.phone, message))
    for i in recepient_lst:
        send_request(str(i[0]), i[1])
        index += 1
    if index == len(recepient_lst):
        send(url, data1)
    send(url, data2)



@shared_task
def send_request2():
    url = '...'
    data1 = {'message': "Sent"}
    data2 = {'message': "No sent"}
    recepient_lst = []
    message = Mailing.objects.all().get(pk=2).message
    index = 1
    for i in Clientt.objects.all():
        recepient_lst.append((i.phone, message))
    for i in recepient_lst:
        send_request(str(i[0]), i[1])
        index += 1
    if index == len(recepient_lst):
        send(url, data1)
    send(url, data2)

@shared_task
def send_request3():
    url = '...'
    data1 = {'message': "Sent"}
    data2 = {'message': "No sent"}
    recepient_lst = []
    message = Mailing.objects.all().get(pk=3).message
    index = 1
    for i in Clientt.objects.all():
        recepient_lst.append((i.phone, message))
    for i in recepient_lst:
        send_request(str(i[0]), i[1])
        index += 1
    if index == len(recepient_lst):
        send(url, data1)
    send(url, data2)