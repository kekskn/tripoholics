# Generated by Django 4.1.1 on 2022-12-11 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_addtravel_myuser_addtravel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='bio',
        ),
    ]
