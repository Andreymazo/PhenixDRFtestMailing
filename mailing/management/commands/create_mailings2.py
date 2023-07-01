from django.core.management import BaseCommand

from mailing.models import Clientt, Mailing

import random
from datetime import datetime, timedelta


def rand_date():
    start = datetime.now()
    end = start + timedelta(days=2)
    random_date = start - (end - start) * random.random()
    return random_date


lst_clientt = ['message 1', 'message 2', 'message 3']


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in lst_clientt:
            mailing = Mailing.objects.create(
                last_attempt=rand_date(),
                message=f'{i}',
                time_completion=rand_date(),
                tag='921',

            )

            mailing.save()
