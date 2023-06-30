from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientList, ClientCreate

app_name = MailingConfig.name

urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('', ClientList.as_view(), name='home'),
    path('client_create', ClientCreate.as_view(), name='client_create'),
]
