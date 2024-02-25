from .models import camp_info
from django.shortcuts import render


# Create your views here.
def home(request):
    locations = camp_info.objects.all()
    return render(request, 'home.html', {'locations': locations})

