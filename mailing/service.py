import os
from smtplib import SMTPResponseException, SMTPRecipientsRefused
from mailing.models import Mailinglog, Clientt, Mailinglog_request
import requests

url = '...'
data = {}


def send_request(recepient, mssg):  # request,

    login = os.getenv('SMS_login')
    password = os.getenv('SMS_password')
    api_id = os.getenv('api_id')
    url = f'https://sms.ru/sms/send?api_id={api_id}&to={recepient}&msg={mssg}&json=1'
    pag = requests.get(
            url)

    if pag.status_code == 200:
        print(pag.json())
        Mailinglog.objects.create(
            ####Zapisivaem pochtu, resultat otpravki i vremia samo zapisivaetsia#########
            mailing=recepient,
            result=pag.status_code
        )

    print(pag.status_code, pag.content, pag.text, pag.json())


def send(user_url, userdata):
    try:
        res = requests.post(url=user_url, data=userdata)

        if res:
            Mailinglog_request.objects.create(
                mailing=user_url,
                result=res
            )
    except SMTPResponseException as e:
        pass
    except SMTPRecipientsRefused as e:
        print(e)
        pass
