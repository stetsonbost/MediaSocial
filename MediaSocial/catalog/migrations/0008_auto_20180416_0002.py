# Generated by Django 2.0.3 on 2018-04-16 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180413_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateField(default=datetime.date(2018, 4, 16)),
        ),
        migrations.AlterField(
            model_name='television',
            name='first_air_date',
            field=models.DateField(default=datetime.date(2018, 4, 16)),
        ),
    ]
