# Generated by Django 4.1.1 on 2022-12-01 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0006_addtravel_myuser_alter_myprofile_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtravel',
            name='myuser',
        ),
        migrations.AddField(
            model_name='addtravel',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]