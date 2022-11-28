from django.db import models
from django_countries.fields import Countries
from django.contrib.auth.models import User



class MyUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User Email')

class MyProfile(models.Model):
    myuser = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.myuser.first_name} Profile'