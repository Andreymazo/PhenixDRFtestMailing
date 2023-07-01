from rest_framework import serializers

from mailing.models import Clientt


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientt
        fields = '__all__'
