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


# class Client(models.Model):  # ):AbstractBaseUser, PermissionsMixin
#
#     TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
#
#     # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     # phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
#     #                                  "The phone number provided is invalid")
#     email = models.EmailField(max_length=100, unique=True)
#     # VERIFICATION_TYPE = [
#     #     ('sms', 'SMS'),
#     # ]
#     # phone_number = PhoneNumberField(unique = True)
#     # verification_method = models.CharField(max_length=10,choices= VERIFICATION_TYPE)
#     phone = PhoneNumberField(unique=True, **NULLABLE)
#
#     # phone_number = models.CharField(max_length=16, validators=[phone_validator], unique=True, verbose_name='телефон')
#
#     country_phone_code = models.CharField(default=None, editable=False, max_length=4,
#                                           verbose_name='код мобильного оператора')
#
#     # full_name = models.CharField(max_length=30)
#     # is_superuser = models.BooleanField(default=False)
#     # is_staff = models.BooleanField(default=False)
#     # is_active = models.BooleanField(default=True)
#     # is_emailed = models.BooleanField(default=False)
#     # is_phoned = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     # client_timezone = TimeZoneField(
#     #     use_pytz=True)  # returns pytz timezone objects#https://github.com/mfogel/django-timezone-field?files=1#  Мешает создавать пользователей поле is not JSON serializable
#     client_timezone = models.CharField(
#         verbose_name="Time zone", max_length=32, choices=TIMEZONES, default="UTC"
#     )
#
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = []
#     # objects = ClientUserManager()
#
#     # def __str__(self):
#     #     return self.email
#     #
#     # @staticmethod
#     # def has_perm(perm, obj=None, **kwargs):
#     #     return True
#     #
#     # @staticmethod
#     # def has_module_perms(app_label, **kwargs):
#     #     return True
#     def save(self, *args, **kwargs):
#         self.country_phone_code = str(self.phone)[1:4]
#         return super(Client, self).save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = "Client"
#         verbose_name_plural = "Clients"


class Mailing(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    last_attempt = models.DateTimeField(auto_now=True)
    message = models.TextField()
    tag = models.CharField(verbose_name='фильтр свойств клиентов, код оператора')
    time_completion = models.DateTimeField(auto_now=True)
    # client = models.ForeignKey('mailing.Clientt', on_delete=models.CASCADE, related_name='mailing')


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
    mailing = models.CharField(max_length=100, verbose_name='Email')
    result = models.CharField(max_length=100, verbose_name='Result')
    last_attempt = models.DateTimeField(auto_now=True)
