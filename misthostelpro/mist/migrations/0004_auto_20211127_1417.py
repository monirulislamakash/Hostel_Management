# Generated by Django 3.2.6 on 2021-11-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0003_notice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_history',
            name='Fixed_Food',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='payment_history',
            name='Ledge_Development',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='payment_history',
            name='Mobile',
            field=models.IntegerField(default=880, max_length=50),
        ),
        migrations.AddField(
            model_name='payment_history',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='payment_history',
            name='Resiver',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='payment_history',
            name='Amount',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
