# Generated by Django 3.2 on 2023-03-18 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_myprofile_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='last_online_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
