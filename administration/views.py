from django.shortcuts import render
from administration.models import camp_details
import json
# Create your views here.
def index(request):
    camps = camp_details.objects.all()
    camp_data = [{'lat': camp.lattitude, 'lng': camp.longitude, 'description': camp.description} for camp in camps]
    return render(request, 'index.html', {'camp_data': json.dumps(camp_data)})