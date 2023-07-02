from rest_framework import serializers

from mailing.models import Clientt, Mailing, Mailinglog


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientt
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    last_attempt = serializers.ReadOnlyField()

    class Meta:
        model = Mailing
        fields = '__all__'
class MailinglogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailinglog
        fields = '__all__'