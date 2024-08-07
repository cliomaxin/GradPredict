from django.shortcuts import render, redirect
from .models import studentUser
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Email is already in use. Please use another one.')
                    return redirect('index')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.info(request, 'You have successfully created an account. Please sign in.')
                    return redirect('index')
            else:
                messages.info(request, 'Passwords do not match! Create account again')
                return redirect('index')
        
        elif action == 'signin':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('studentDetailscapture')
            else:
                messages.info(request, 'The account does not exist! Make sure you have typed your name in the correct capitalization OR create an account and try again')
                return redirect('index')
    
    return render(request, 'dashboard.html')

@login_required
def studentDetailscapture(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        student_id = request.POST.get('student_id')
        program_entrance = request.POST.get('program_entrance')
        mode_of_learning = request.POST.get('mode_of_learning')

        # Save the data to the model
        studentDetails = studentUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone_number=phone_number,
            student_id=student_id,
            program_entrance=program_entrance,
            mode_of_learning=mode_of_learning,
        )
        studentDetails.save()
        return redirect('success')
    else:
         context = {
         }
         return render(request, 'studentform.html', {'context': context})

@login_required    
def logout(request):
    auth.logout(request)
    return redirect('/') 

def success(request):
    # Retrieve all details from the database
    # all_details = studentUser.objects.all().order_by('-created_at') 
    context={
        #  'details_list': all_details,
    }
    return render(request, 'success.html', context)








































