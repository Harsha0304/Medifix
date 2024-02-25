from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(), name='login'),
    path('home', views.home, name="home"),
]
