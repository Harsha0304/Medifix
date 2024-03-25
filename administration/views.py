from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, ProfileForm
from django.core.mail import send_mail
from django.conf import settings
from .models import profile, camp_details
import json
# Create your views here.
def index(request):
    
    return render(request,'index.html')

@login_required
def home(request):
    camps = camp_details.objects.all()
    camp_data = [{'lat': camp.lattitude, 'lng': camp.longitude, 'description': camp.description} for camp in camps]
    return render(request, 'home.html', {'camp_data': json.dumps(camp_data)})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            subject = 'Welcome to Our Website!'
            message = 'Dear {},\n\nThank you for registering on our website. You are now able to log in.\n\nBest regards,\nThe Website Team'.format(user.username)
            from_email = settings.EMAIL_HOST_USER
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])


            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'register_form': form})

def register_camp_org(request):
    user_profile = profile.objects.get(user_name=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            user_profile.submitted_application = True
            user_profile.save()

            user_email_subject = 'Camp Organizer Registration Submission Acknowledgement'
            user_email_message = 'Dear {},\n\nYour request for registering as a camp organizer has been received. We will review your application shortly.\n\nThank you for your interest.\n\nBest regards,\nThe Camp Registration Team'.format(request.user.username)
            send_mail(user_email_subject, user_email_message, settings.EMAIL_HOST_USER, [request.user.email])

            subject = 'New Camp Organizer Registration Request'
            message = 'User {} has requested for registering as a camp organizer. Please take appropriate action.'.format(request.user.username)
            from_email = settings.EMAIL_HOST_USER
            to_email = settings.SUPER_ADMIN_EMAIL
            send_mail(subject, message, from_email, [to_email])

            return redirect('camp_register')
    else:
        form = ProfileForm(instance=user_profile)
    
    submitted_application = user_profile.submitted_application
    camp_register = user_profile.camp_register
    return render(request, 'camp_register.html', {'form': form, 'submitted_application': submitted_application, 'camp_register': camp_register})

def user_camps(request):
    user_camps = camp_details.objects.filter(createdby=request.user)
    return render(request, 'camp/all_camps_user.html', {'user_camps': user_camps})