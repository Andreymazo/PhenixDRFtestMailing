from django.core.management import BaseCommand

from mailing.models import Clientt, Mailing

lst_clientt = [('+79219507382', Mailing.objects.get(pk=1)), ('+79319505382',Mailing.objects.get(pk=2)), ('+79219507389',Mailing.objects.get(pk=3))]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in lst_clientt:
            user = Clientt.objects.create(
                phone=i[0],
                country_phone_code=f'{i}'[5:6],
                mailing=i[1]

            )

            user.save()
