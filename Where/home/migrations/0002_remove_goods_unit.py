# Generated by Django 2.0.1 on 2018-03-07 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='unit',
        ),
    ]