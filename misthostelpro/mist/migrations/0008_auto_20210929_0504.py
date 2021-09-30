# Generated by Django 3.2.6 on 2021-09-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0007_meal_order_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='afternoon_meal',
            name='When',
            field=models.CharField(default='Lunch', max_length=30, verbose_name='Lunch'),
        ),
        migrations.AddField(
            model_name='denar_meal',
            name='When',
            field=models.CharField(default='Dinner', max_length=30, verbose_name='Dinner'),
        ),
        migrations.AddField(
            model_name='morning_meal',
            name='When',
            field=models.CharField(default='breakfast', max_length=30, verbose_name='breakfast'),
        ),
    ]