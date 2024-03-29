# Generated by Django 3.2 on 2023-03-11 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFutureTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_where', models.CharField(max_length=100)),
                ('to_where', models.CharField(max_length=100)),
                ('transport_type', models.CharField(choices=[('Plane', 'plane'), ('Train', 'train'), ('Bus', 'bus'), ('Car', 'car'), ('Bike', 'bike'), ('Hitchhike', 'hitchhike'), ('Ship', 'ship'), ('Other', 'other')], max_length=100)),
                ('how_long_traveled', models.IntegerField()),
                ('with_whom', models.CharField(choices=[('Alone', 'alone'), ('Couple', 'couple'), ('With friend', 'with friend'), ('Group of friends', 'group of friends'), ('Family', 'family'), ('Colleagues (work/college/school)', 'colleagues (work/college/school)')], max_length=100)),
                ('accommodation', models.CharField(choices=[('Hotel', 'hotel'), ('Hostel', 'hostel'), ('Camping', 'camping'), ('Apartments', 'apartments'), ('RV', 'RV'), ('Friends/family', 'friends/family'), ('Hospitality exchange services', 'hospitality exchange services'), ('Other', 'other')], max_length=100)),
                ('reason', models.CharField(choices=[('Leisure', 'leisure'), ('Snow and ski', 'snow and ski'), ('Sun and beach', 'sun and beach'), ('Event travel', 'event travel'), ('Nature travel', 'nature travel'), ('Adventure travel', 'adventure travel'), ('City break', 'city break'), ('Food and wine', 'food and wine'), ('Volunteer work', 'volunteer work'), ('Business', 'business')], max_length=100)),
                ('money_spent', models.CharField(choices=[('150', '150'), ('150-300', '150-300'), ('300-500', '300-500'), ('500-1000', '500-1000'), ('1000-3000', '1000-3000'), ('3000+', '3000+')], max_length=100)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddPastTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_where', models.CharField(max_length=100)),
                ('to_where', models.CharField(max_length=100)),
                ('transport_type', models.CharField(choices=[('Plane', 'plane'), ('Train', 'train'), ('Bus', 'bus'), ('Car', 'car'), ('Bike', 'bike'), ('Hitchhike', 'hitchhike'), ('Ship', 'ship'), ('Other', 'other')], max_length=100)),
                ('how_long_traveled', models.IntegerField()),
                ('with_whom', models.CharField(choices=[('Alone', 'alone'), ('Couple', 'couple'), ('With friend', 'with friend'), ('Group of friends', 'group of friends'), ('Family', 'family'), ('Colleagues (work/college/school)', 'colleagues (work/college/school)')], max_length=100)),
                ('accommodation', models.CharField(choices=[('Hotel', 'hotel'), ('Hostel', 'hostel'), ('Camping', 'camping'), ('Apartments', 'apartments'), ('RV', 'RV'), ('Friends/family', 'friends/family'), ('Hospitality exchange services', 'hospitality exchange services'), ('Other', 'other')], max_length=100)),
                ('reason', models.CharField(choices=[('Leisure', 'leisure'), ('Snow and ski', 'snow and ski'), ('Sun and beach', 'sun and beach'), ('Event travel', 'event travel'), ('Nature travel', 'nature travel'), ('Adventure travel', 'adventure travel'), ('City break', 'city break'), ('Food and wine', 'food and wine'), ('Volunteer work', 'volunteer work'), ('Business', 'business')], max_length=100)),
                ('money_spent', models.CharField(choices=[('150', '150'), ('150-300', '150-300'), ('300-500', '300-500'), ('500-1000', '500-1000'), ('1000-3000', '1000-3000'), ('3000+', '3000+')], max_length=100)),
                ('pictures', models.ImageField(default='image.jpg', upload_to='')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AddTravel',
        ),
    ]
