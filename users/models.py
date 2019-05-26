from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.
class CustomUser(AbstractUser):

    password = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, max_length=255)
    dob = models.CharField(blank=True, max_length=255)

    # def __str__(self):
    #     return '{} {}'.format(self.User.fist_name, self.User.last_name)