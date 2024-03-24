from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'register_form': form})