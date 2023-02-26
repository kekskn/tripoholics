from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class MyUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User Email')

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField()
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            MyProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.myprofile.save()


TRANSPORT = (
    ("Plane", "plane"),
    ("Train", "train",),
    ("Bus", "bus"),
    ("Car", 'car'),
    ("Bike", 'bike'),
    ("Hitchhike", 'hitchhike'),
    ("Ship", 'ship'),
    ("Other", 'other'),
)

COMPANY = (
    ("Alone", "alone"),
    ("Couple", "couple",),
    ("With friend", "with friend"),
    ("Group of friends", 'group of friends'),
    ("Family", 'family'),
    ("Colleagues (work/college/school)", 'colleagues (work/college/school)'),
)

ACCOMMODATION = (
    ("Hotel", "hotel"),
    ("Hostel", "hostel",),
    ("Camping", "camping"),
    ("Apartments", 'apartments'),
    ("RV", 'RV'),
    ("Friends/family", 'friends/family'),
    ("Hospitality exchange services", 'hospitality exchange services'),
    ("Other", 'other'),
)

REASON = (
    ("Leisure", "leisure"),
    ("Snow and ski", "snow and ski",),
    ("Sun and beach", "sun and beach"),
    ("Event travel", 'event travel'),
    ("Nature travel", 'nature travel'),
    ("Adventure travel", 'adventure travel'),
    ("City break", 'city break'),
    ("Food and wine", 'food and wine'),
    ("Volunteer work", 'volunteer work'),
    ("Business", 'business'),
)

MONEY_SPENT = (
    ("150", "150"),
    ("150-300", "150-300",),
    ("300-500", "300-500"),
    ("500-1000", '500-1000'),
    ("1000-3000", '1000-3000'),
    ("3000+", '3000+'),
)



class AddPastTravel(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    from_where = models.CharField(max_length=100)
    to_where = models.CharField(max_length=100)
    transport_type = models.CharField(choices=TRANSPORT, max_length=100)
    when_traveled = models.DateField
    how_long_traveled = models.IntegerField()
    with_whom = models.CharField(choices=COMPANY, max_length=100)
    accommodation = models.CharField(choices=ACCOMMODATION, max_length=100)
    reason = models.CharField(choices=REASON, max_length=100)
    money_spent = models.CharField(choices=MONEY_SPENT, max_length=100)
    pictures = models.ImageField(default='image.jpg')

class AddFutureTravel(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    from_where = models.CharField(max_length=100)
    to_where = models.CharField(max_length=100)
    transport_type = models.CharField(choices=TRANSPORT, max_length=100)
    when_traveled = models.DateField
    how_long_traveled = models.IntegerField()
    with_whom = models.CharField(choices=COMPANY, max_length=100)
    accommodation = models.CharField(choices=ACCOMMODATION, max_length=100)
    reason = models.CharField(choices=REASON, max_length=100)
    money_spent = models.CharField(choices=MONEY_SPENT, max_length=100)





