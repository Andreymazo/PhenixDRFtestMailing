import django_filters

from mailing.models import Mailinglog


class MailinglogFilter(django_filters.FilterSet):
    mailing = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Mailinglog
        ordering = ('mailing',)
        fields = ['mailing', ]
