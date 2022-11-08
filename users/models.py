from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('family', 'family'),
        ('moderator', 'moderator')
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    name = models.CharField(max_length=50)
    name_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name




