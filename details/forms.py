from django import forms
from .models import studentUser

class studentUser(forms.ModelForm):
    class Meta:
        model = studentUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone_number', 'student_id', 'program_entrance', 'mode_of_learning', 'profile_picture']
