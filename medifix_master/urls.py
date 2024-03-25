from django.contrib import admin
from django.urls import path, include
from administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('register/', views.signup_view, name="register"),
    path('camp_register/', views.register_camp_org, name="camp_register"),
]
