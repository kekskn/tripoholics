# Generated by Django 3.2 on 2023-02-25 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientApi', '0004_message_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]