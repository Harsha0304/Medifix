from django.contrib import admin
from .models import camp_info, doctor_info, profile, experience, education
# Register your models here.

admin.site.register(camp_info)
admin.site.register(doctor_info)
admin.site.register(profile)
admin.site.register(experience)
admin.site.register(education)
