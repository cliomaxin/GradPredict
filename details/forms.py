from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import studentUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = studentUser
        fields = ('username', 'email', 'student_id', 'password1', 'password2', 'year_of_study', 'gender')

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label="Email")