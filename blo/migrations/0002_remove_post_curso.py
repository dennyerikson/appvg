# Generated by Django 2.1.3 on 2018-11-21 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='curso',
        ),
    ]
