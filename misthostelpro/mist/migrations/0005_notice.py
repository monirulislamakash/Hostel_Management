# Generated by Django 3.2.6 on 2021-09-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mist', '0004_meal_order_hostel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titel', models.CharField(default='', max_length=50)),
                ('Body', models.TextField()),
            ],
        ),
    ]