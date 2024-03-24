from django.contrib import admin
from administration import models
# Register your models here.
admin.site.register(models.profile)
admin.site.register(models.doctor)
admin.site.register(models.camp_details)