# Generated by Django 3.0.8 on 2020-07-03 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
    ]
