from rest_framework import serializers

from mailing.models import Clientt, Mailing, Mailinglog


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientt
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    phone = ClientSerializer(source='clientt', many=False)

    class Meta:
        model = Mailing
        fields = ['message', 'tag', 'last_attempt', 'time_completion', 'phone']


class MailinglogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailinglog
        fields = '__all__'
