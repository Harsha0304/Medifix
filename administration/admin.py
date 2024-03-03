from django.contrib import admin
from administration import models
# Register your models here.
admin.site.register(models.profile)
admin.site.register(models.doctor)
admin.site.register(models.education)
admin.site.register(models.license_certification)
admin.site.register(models.Skill)
admin.site.register(models.skills_selection)
admin.site.register(models.experience)
admin.site.register(models.Project)