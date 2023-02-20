from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class MyUser(models.Model):
    # user_id = models.AutoField(primary_key=True)
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
    ("1", "plane"),
    ("2", "train",),
    ("3", "bus"),
    ("4", 'car'),
    ("5", 'bike'),
    ("6", 'hitchhike'),
    ("7", 'ship'),
    ("8", 'other'),
)

COMPANY = (
    ("1", "alone"),
    ("2", "couple",),
    ("3", "with friend"),
    ("4", 'group of friends'),
    ("5", 'family'),
    ("6", 'colleagues (work/college/school)'),
)

ACCOMMODATION = (
    ("1", "hotel"),
    ("2", "hostel",),
    ("3", "camping"),
    ("4", 'apartments'),
    ("5", 'RV'),
    ("6", 'friends/family'),
    ("7", 'hospitality exchange services'),
    ("8", 'other'),
)

REASON = (
    ("1", "leisure"),
    ("2", "snow and ski",),
    ("3", "sun and beach"),
    ("4", 'event travel'),
    ("5", 'nature travel'),
    ("6", 'adventure travel'),
    ("7", 'city break'),
    ("8", 'food and wine'),
    ("9", 'volunteer work'),
    ("10", 'business'),
)

MONEY_SPENT = (
    ("1", "150"),
    ("2", "150-300",),
    ("3", "300-500"),
    ("4", '500-1000'),
    ("5", '1000-3000'),
    ("6", '3000+'),
)



class AddTravel(models.Model):
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




