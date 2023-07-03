import datetime
from celery import shared_task

from config.celery import app
from mailing.models import Clientt, Mailing

from mailing.service import send, send_request

a = False
b = False
c = False


# @app.task
@shared_task
def send_request1():
    global a
    sending = Mailing.objects.all().get(pk=1)
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

    if sending.last_attempt <= datetime.datetime.now() <= sending.time_completion:
        a = True


@shared_task
def send_request2():
    global b
    sending = Mailing.objects.all().get(pk=2)
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
    if sending.last_attempt <= datetime.datetime.now() <= sending.time_completion:
        b = True


@shared_task
def send_request3():
    global c
    sending = Mailing.objects.all().get(pk=3)
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
    if sending.last_attempt <= datetime.datetime.now() <= sending.time_completion:
        c = True


@shared_task
def send_request3():
    """Если рассылки по рассылкам закончены, то отсылаем какое-то уведомление"""
    global a
    global b
    global c
    url = '...'
    data = {'message': "Sent"}
    while a and b and c:
        send(url, data)
    a = False
    b = False
    c = False