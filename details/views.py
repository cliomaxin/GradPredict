from django.shortcuts import render, redirect
from .models import studentUser
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from .forms import SignUpForm, SignInForm
import re
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':
            student_name = request.POST['student_name']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Email is already in use. Please use another one.')
                    return redirect('index')
                else:
                    user = User.objects.create_user(username=username, student_name=student_name, password=password)
                    user.save()
                    messages.info(request, 'You have successfully created an account. Please sign in.')
                    return redirect('index')
            else:
                messages.info(request, 'Passwords do not match!')
                return redirect('index')
        
        elif action == 'signin':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('view')
            else:
                messages.info(request, 'The account does not exist. Please try again!')
                return redirect('index')
    
    return render(request, 'dashboard.html')

@login_required    
def logout(request):
    auth.logout(request)
    return redirect('/') 

def view(request):
    # Retrieve all details from the database
    all_details = studentUser.objects.all().order_by('-created_at')
    
    context={
         'details_list': all_details,
    }
    return render(request, 'view.html', context)








































