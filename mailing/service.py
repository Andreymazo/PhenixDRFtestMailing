import os
from smtplib import SMTPResponseException, SMTPRecipientsRefused

from django.core.mail import send_mail
from django.shortcuts import render

from config import settings
from mailing.models import Mailinglog, Clientt
import requests

url = '...'
data = {}


def send_request(recepient, mssg):  # request,
    # if request.method == "POST" or "GET":
    #     print('recepient================')
    #     __secret = ''
    #     login = os.getenv('SMS_login')
    #     password = os.getenv('SMS_password')
    #     api_id = os.getenv('api_id')
    login = os.getenv('SMS_login')
    password = os.getenv('SMS_password')
    api_id = os.getenv('api_id')
    # for i in Clientt.objects.all():
    #     recepient = str(i.phone)

        # recepient = str(Clientt.objects.get(phone=request.user.phone).phone)
        # print('type(recepient1), recepient1', type(recepient1), recepient1.phone_number)
        # recepient2 = CustomUser.objects.all().filter(phone_number=request.user.phone_number).values('phone_number').get('phone_number')
        # print('recepient================', recepient1, recepient2.values(), type(recepient1))
        # print('recepient================', recepient2)
        ########################################## Нижние 4 рабочие урлы Megafon #######################################
        # url = f'https://sms.ru/auth/check?api_id={api_id}&json=1'
    url = f'https://sms.ru/auth/check?login={login}&password={password}&json=1'
        # url = f'https://sms.ru/sms/send?api_id={api_id}&to={recepient}&msg={mssg}&json=1'

        # url = f'https://sms.ru/sms/cost?api_id={api_id}&to[79219507391]=hello+world&to[74993221627]=hello+world&json=1'
        ##########################################################################################################
        # pass
    pag = requests.get(
            url)  # , headers=headers)#, headers=headers)#, auth=HTTPDigestAuth(login, password), headers=headers, timeout=5)

    if pag.status_code == 200:
        print(pag.json())
    print(pag.status_code, pag.content, pag.text, pag.json())


def send(user_url):
    try:
        res = requests.post(url=url, data=data)

        if res:
            Mailinglog.objects.create(
                ####Zapisivaem url, resultat otpravki i vremia samo zapisivaetsia#########
                mailing=user_url,
                result=res
            )
    except SMTPResponseException as e:
        pass
    except SMTPRecipientsRefused as e:
        print(e)
        pass
