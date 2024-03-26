from django.db import models

# Create your models here.
class details(models.Model):
    student_name = models.CharField(max_length=150, default="")
    student_email = models.CharField(max_length=150, default="")
    admission_number = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.student_name