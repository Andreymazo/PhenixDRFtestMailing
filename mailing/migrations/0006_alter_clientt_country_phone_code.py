# Generated by Django 4.2.2 on 2023-07-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_alter_clientt_country_phone_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientt',
            name='country_phone_code',
            field=models.CharField(max_length=4, verbose_name='код мобильного оператора'),
        ),
    ]
