# Generated by Django 4.1.1 on 2022-12-11 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_remove_myprofile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='image',
        ),
    ]
