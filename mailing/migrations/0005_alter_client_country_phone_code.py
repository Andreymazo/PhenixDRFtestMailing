# Generated by Django 4.2.2 on 2023-06-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_remove_client_client_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='country_phone_code',
            field=models.CharField(default=None, editable=False, max_length=4, verbose_name='код мобильного оператора'),
        ),
    ]
