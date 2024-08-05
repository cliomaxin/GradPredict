from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class studentUser(models.Model):
    student_name = models.CharField(max_length=20, default="", blank=True, null=True)
    username = models.CharField(max_length=100, default="", blank=True, null=True)
    student_id = models.CharField(max_length=20, unique=True, default="", blank=True, null=True)
    year_of_study = models.IntegerField(default="", blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default="2", blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.student_name
    
