# Generated by Django 3.2.6 on 2021-11-28 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0005_auto_20211128_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_history',
            old_name='Resiver',
            new_name='Receiver',
        ),
    ]
