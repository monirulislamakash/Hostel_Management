# Generated by Django 3.2.6 on 2021-09-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0010_profilupdate_permissio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilupdate',
            name='permissio',
        ),
        migrations.AlterField(
            model_name='profilupdate',
            name='permission',
            field=models.BooleanField(default=False),
        ),
    ]