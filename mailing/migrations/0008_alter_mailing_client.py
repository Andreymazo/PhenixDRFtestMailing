# Generated by Django 4.2.2 on 2023-07-01 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_alter_clientt_country_phone_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='mailing.clientt'),
            preserve_default=False,
        ),
    ]
