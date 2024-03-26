from django.shortcuts import render, redirect
from .models import details

# Create your views here.

def index(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        admission_number = request.POST.get('admission_number')
        student_email = request.POST.get('student_email')
        phone_number = request.POST.get('phone_number')
        
        # Create a new instance of the details model and save
        user_details = details(student_name=student_name, admission_number=admission_number, phone_number=phone_number, student_email=student_email)
        user_details.save()
        # Redirect to the view.html page
        return redirect('view')
    return render(request, 'index.html')

def view(request):
    # Retrieve all details from the database
    all_details = details.objects.all().order_by('-created_at')
    
    context={
         'details_list': all_details,
    }
    return render(request, 'view.html', context)










































