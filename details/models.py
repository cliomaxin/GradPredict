from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'Unspecified'),
)

class studentUser(models.Model):
    first_name = models.CharField(max_length=50, default='', blank=True, null=True)
    last_name = models.CharField(max_length=50, default='', blank=True, null=True)
    email = models.CharField(max_length=50, default='', blank=True, null=True)
    gender = models.CharField(max_length=10, default="Unspecified", blank=True,null=True)
    phone_number = models.CharField(max_length=12, default='', blank=True,null=True)
    student_id = models.CharField(max_length=20, default='', blank=True,null=True)
    program_entrance = models.CharField(max_length=20, default='', blank=True,null=True)
    mode_of_learning = models.CharField(max_length=20, default='', blank=True,null=True)

    def __str__(self):
        return self.email
