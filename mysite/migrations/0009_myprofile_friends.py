# Generated by Django 4.1.7 on 2023-04-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='mysite.myprofile'),
        ),
    ]
