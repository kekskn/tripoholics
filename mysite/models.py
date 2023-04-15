from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.cache import cache

class MyUser(models.Model):
    # user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User Email')

class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_online_at = models.DateTimeField(null=True, default=timezone.now)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_pics/")
    country = models.CharField(max_length=50, default='Country')
    friends = models.ManyToManyField("self", blank=True, symmetrical=False)


    # bio = models.TextField()
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'

    @property
    def following(self):
        return MyProfile.objects.filter(followers__follower=self)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            MyProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.myprofile.save()


class Follow(models.Model):
    follower = models.ForeignKey(MyProfile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(MyProfile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')


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
    ("150", 150),
    ("150-300", 225),
    ("300-500", 400),
    ("500-1000", 750),
    ("1000-3000", 2000),
    ("3000+", 3500),
)


class AddPastTravel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    from_where = CountryField(default='Choose', null=True)
    to_where = CountryField(default='Choose', null=True)
    transport_type = models.CharField(choices=TRANSPORT, max_length=100)
    when_traveled = models.DateField()
    how_long_traveled = models.IntegerField()
    with_whom = models.CharField(choices=COMPANY, max_length=100)
    accommodation = models.CharField(choices=ACCOMMODATION, max_length=100)
    reason = models.CharField(choices=REASON, max_length=100)
    money_spent = models.CharField(choices=MONEY_SPENT, max_length=100)
    pictures = models.ImageField(default='image.jpg')

    def save(self, *args, **kwargs):
        if not self.pk:
            request = getattr(self, 'request', None)
            if request is not None and request.user.is_authenticated:
                self.user = request.user
        super().save(*args, **kwargs)


class AddFutureTravel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    from_where = CountryField(default='Choose', null=True)
    to_where = CountryField(default='Choose', null=True)
    transport_type = models.CharField(choices=TRANSPORT, max_length=100)
    when_traveled = models.DateField()
    how_long_traveled = models.IntegerField()
    with_whom = models.CharField(choices=COMPANY, max_length=100)
    accommodation = models.CharField(choices=ACCOMMODATION, max_length=100)
    reason = models.CharField(choices=REASON, max_length=100)
    money_spent = models.CharField(choices=MONEY_SPENT, max_length=100)
