# class ClientList()
from rest_framework import generics

from mailing.models import Clientt
from mailing.serializers import ClientSerializer


class ClienttList(generics.ListCreateAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer


class ClienttCreate(generics.CreateAPIView):
    queryset = Clientt.objects.all()
    serializer_class = ClientSerializer
