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
    path('my_camps/', views.user_camps, name="my_camps"),
    path('camp_organizer_request/', views.camp_organizer_request, name="camp_organizer_request"),
    path('organizer/<str:username>/', views.camp_organizer_profile_detail, name='organizer_user_profile_detail'),
    path('approve/<str:username>/', views.approve_application, name='approve_application'),
    path('deny/<str:username>/', views.deny_application, name='deny_application'),
]
