from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClienttList, ClienttCreate

app_name = MailingConfig.name

urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('', ClienttList.as_view(), name='home'),
    path('client_create', ClienttCreate.as_view(), name='client_create'),
]
