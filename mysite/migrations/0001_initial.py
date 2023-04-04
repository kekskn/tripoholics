# Generated by Django 4.1.3 on 2023-02-18 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_where', models.CharField(max_length=100)),
                ('to_where', models.CharField(max_length=100)),
                ('transport_type', models.CharField(
                    choices=[('1', 'plane'), ('2', 'train'), ('3', 'bus'), ('4', 'car'), ('5', 'bike'),
                             ('6', 'hitchhike'), ('7', 'ship'), ('8', 'other')], max_length=100)),
                ('how_long_traveled', models.IntegerField()),
                ('with_whom', models.CharField(
                    choices=[('1', 'alone'), ('2', 'couple'), ('3', 'with friend'), ('4', 'group of friends'),
                             ('5', 'family'), ('6', 'colleagues (work/college/school)')], max_length=100)),
                ('accommodation', models.CharField(
                    choices=[('1', 'hotel'), ('2', 'hostel'), ('3', 'camping'), ('4', 'apartments'), ('5', 'RV'),
                             ('6', 'friends/family'), ('7', 'hospitality exchange services'), ('8', 'other')],
                    max_length=100)),
                ('reason', models.CharField(
                    choices=[('1', 'leisure'), ('2', 'snow and ski'), ('3', 'sun and beach'), ('4', 'event travel'),
                             ('5', 'nature travel'), ('6', 'adventure travel'), ('7', 'city break'),
                             ('8', 'food and wine'), ('9', 'volunteer work'), ('10', 'business')], max_length=100)),
                ('money_spent', models.CharField(
                    choices=[('1', '150'), ('2', '150-300'), ('3', '300-500'), ('4', '500-1000'), ('5', '1000-3000'),
                             ('6', '3000+')], max_length=100)),
                ('pictures', models.ImageField(default='image.jpg', upload_to='')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
