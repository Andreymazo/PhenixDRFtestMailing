import datetime
import uuid

import pytz
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


# class ClientUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)
#

class Clientt(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone = PhoneNumberField(unique=True, **NULLABLE)
    country_phone_code = models.CharField(max_length=5,
                                          verbose_name='код мобильного оператора')
    date_joined = models.DateTimeField(default=timezone.now)
    client_timezone = models.CharField(verbose_name="Time zone", max_length=32, choices=TIMEZONES, default="UTC")
    mailing = models.ForeignKey('mailing.Mailing', on_delete=models.CASCADE, related_name='clientt', **NULLABLE)

    def save(self, *args, **kwargs):
        self.country_phone_code = str(self.phone)[2:5]
        return super(Clientt, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Mailing(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    last_attempt = models.DateTimeField(auto_now=True)
    message = models.TextField(verbose_name='text')
    tag = models.CharField(verbose_name='фильтр свойств клиентов, код оператора')
    time_completion = models.DateTimeField(auto_now=True)

    # client = models.ForeignKey('mailing.Clientt', on_delete=models.CASCADE, related_name='mailing')

    def __str__(self):
        return f"Mailing {self.pk}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Message(models.Model):
    STATUS_DONE = True
    STATUS_NO_DONE = False
    STATUSES = (
        (STATUS_DONE, 'Отправлено'),
        (STATUS_NO_DONE, 'Не отправлено')
    )
    status = models.BooleanField(choices=STATUSES, verbose_name='Статус сообщения',
                                 default=STATUS_NO_DONE)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    last_attempt = models.DateTimeField(auto_now=True)
    mailing = models.ForeignKey('mailing.Mailing', on_delete=models.CASCADE, related_name="mess")
    client = models.ForeignKey('mailing.Clientt', on_delete=models.CASCADE, related_name="message")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Mailinglog(models.Model):
    mailing = models.CharField(max_length=20, verbose_name='Phone of a client')
    result = models.CharField(max_length=100, verbose_name='Result')
    last_attempt = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=3, verbose_name='Code mobile operator')

    def save(self, *args, **kwargs):
        self.tag = str(self.mailing)[2:5]
        return super(Mailinglog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Mailing statistic"
        verbose_name_plural = "Mailing statistics"


class Mailinglog_request(models.Model):
    mailing = models.CharField(max_length=100, verbose_name='Email')
    result = models.CharField(max_length=100, verbose_name='Result')
    last_attempt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Request statistic"
        verbose_name_plural = "Request statistics"
