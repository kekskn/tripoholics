# Generated by Django 3.2 on 2023-02-24 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientApi', '0002_currentuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='test',
        ),
    ]
