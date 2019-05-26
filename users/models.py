from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    fname = models.CharField(blank=True, max_length=255)
    lname = models.CharField(blank=True, max_length=255)
    password = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, max_length=255)
    dob = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return '{} {}'.format(self.fname, self.lname)