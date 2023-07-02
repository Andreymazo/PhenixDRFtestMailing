# Generated by Django 4.2.2 on 2023-07-01 15:52

from django.db import migrations, models
import django.db.models.deletion

DEFAULT = 1

# https://ctrlzblog.com/django-migrations-how-to-add-non-nullable-fields-without-compromising-your-database/
def forwards(apps, _):
    Mailing = apps.get_model("mailing", "Mailing")
    mailings = Mailing.objects.all()
    for mailing in mailings:
        mailing.client = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='mailing.clientt')
        mailing.save()


def backwards(apps, _):
    Mailing = apps.get_model("mailings", "Mailing")
    mailings = Mailing.objects.all()
    for mailing in mailings:
        mailing.client = DEFAULT
        mailing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailinglog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='client',
            field=models.ForeignKey(default=DEFAULT, on_delete=django.db.models.deletion.CASCADE, related_name='mailing', to='mailing.clientt'),
            preserve_default=False,
        ),
        migrations.RunPython(forwards, backwards)
    ]