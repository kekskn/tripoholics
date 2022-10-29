from django.db import models
from django_countries.fields import Countries

class MyUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField('User Email')

