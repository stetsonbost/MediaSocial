# Generated by Django 2.0.3 on 2018-03-20 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cID', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=20)),
                ('description', models.CharField(help_text='Enter a comment...', max_length=500)),
            ],
        ),
    ]
