# Generated by Django 4.2.2 on 2023-07-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0011_remove_message_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailinglog_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing', models.CharField(max_length=100, verbose_name='Email')),
                ('result', models.CharField(max_length=100, verbose_name='Result')),
                ('last_attempt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
