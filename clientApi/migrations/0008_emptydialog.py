# Generated by Django 3.2 on 2023-03-11 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApi', '0007_remove_currentuser_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmptyDialog',
            fields=[
                ('dialog_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('interlocutor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interlocutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]