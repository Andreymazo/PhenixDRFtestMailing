# class ClientList()
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from mailing.models import Clientt, Mailing, Mailinglog
from mailing.serializers import ClientSerializer, MailingSerializer, MailinglogSerializer


class ClienttList(generics.ListCreateAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country_phone_code', 'date_joined', 'client_timezone']


class ClienttCreate(generics.CreateAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer


class ClienttUpdate(generics.UpdateAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer


class ClienttDestroy(generics.DestroyAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer


class MailingList(generics.ListAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_attempt']


class MailingCreate(generics.CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingUpdate(generics.UpdateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingDestroy(generics.DestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailinglogList(generics.ListAPIView):
    queryset = Mailinglog.objects.all()
    serializer_class = MailinglogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

