from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClienttList, ClienttCreate, MailingCreate, MailingList, ClienttUpdate, ClienttDestroy, \
    MailingUpdate, MailingDestroy, MailinglogList
from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = MailingConfig.name

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # path('', hello, name='home'),#WRONG
    path('', ClienttList.as_view(), name='home'),
    path('client_create', ClienttCreate.as_view(), name='client_create'),
    path('clientt_update/<int:pk>', ClienttUpdate.as_view(), name='clientt_update'),
    path('сlientt_destroy/<int:pk>', ClienttDestroy.as_view(), name='сlientt_destroy'),

    path('mailing_list', MailingList.as_view(), name='mailing_list'),
    path('mailing_create', MailingCreate.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>', MailingUpdate.as_view(), name='mailing_update'),
    path('mailing_destroy/<int:pk>', MailingDestroy.as_view(), name='mailing_destroy'),
    path('mailinglog_lst', MailinglogList.as_view(), name='mailing_destroy'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]




