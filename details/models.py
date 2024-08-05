from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class studentUser(models.Model):
    student_name = models.CharField(max_length=20, default="", blank=True, null=True)
    student_id = models.CharField(max_length=20, unique=True, default="", blank=True, null=True)
    # year_of_study = models.IntegerField(max_length=20, default="", blank=True, null=True)
    # gender = models.CharField(max_length=10, default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.student_name
    
class UserInfo(models.Model):
    business_name=models.CharField(max_length=300)
    business_email=models.CharField(max_length=300)
    user_ip=models.CharField(max_length=300)
    country = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.business_name