# Generated by Django 2.0.3 on 2018-04-12 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180319_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mediaItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book'),
        ),
    ]
