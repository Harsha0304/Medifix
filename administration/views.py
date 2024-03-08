from django.shortcuts import render
from administration.models import camp_details, doctor, Skill
from django.contrib.auth.models import User
import json
# Create your views here.
def index(request):
    camps = camp_details.objects.all()
    camp_data = [{'lat': camp.lattitude, 'lng': camp.longitude, 'description': camp.description} for camp in camps]
    return render(request, 'index.html', {'camp_data': json.dumps(camp_data)})

def camp_detail(request):
    camp_data = camp_details.objects.all()
    return render(request, 'data/camp_details.html', {'camp_data': camp_data})

def users(request):
    user_data = User.objects.all()
    return render(request, 'data/all_users.html', {'user_data': user_data})

def doctors(request):
    doctor_data = doctor.objects.all()
    return render(request, 'data/all_doctors.html', {'doctor_data': doctor_data})

def skills(request):
    skill_data = Skill.objects.all()
    return render(request, 'data/all_skills.html', {'skill_data': skill_data})