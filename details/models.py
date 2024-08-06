from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'Unspecified'),
)

class studentUser(models.Model):
    first_name = models.CharField(max_length=50, default="", blank=True, null=True)
    last_name = models.CharField(max_length=50, default="", blank=True, null=True)
    email = models.EmailField(default="", blank=True, null=True)
    gender = models.IntegerField(default="Unspecified", blank=True,null=True)
    phone_number = models.CharField(max_length=12, blank=True,null=True)
    student_id = models.CharField(max_length=20, blank=True,null=True)
    program_entrance = models.CharField(max_length=20, blank=True,null=True)
    mode_of_learning = models.CharField(max_length=20, blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True,null=True)

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.first_name
