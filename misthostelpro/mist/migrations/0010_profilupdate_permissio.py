# Generated by Django 3.2.6 on 2021-09-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0009_auto_20210929_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilupdate',
            name='permissio',
            field=models.BooleanField(default=False),
        ),
    ]