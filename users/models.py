from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length= 255)
    username = models.CharField(unique=True,max_length= 200)
    date_of_birth= models.DateField(null=True)
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)

    def __str__(self):
        return self.email
