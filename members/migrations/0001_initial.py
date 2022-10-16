# Generated by Django 4.1.1 on 2022-10-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='First name')),
                ('surname', models.CharField(max_length=25, verbose_name='Last name')),
                ('birth_date', models.DateField(verbose_name='Date of birth')),
                ('city', models.CharField(max_length=30, verbose_name='Hometown')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('password1', models.CharField(max_length=15)),
                ('password2', models.CharField(max_length=15)),
            ],
        ),
    ]
