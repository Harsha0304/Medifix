from django.contrib import admin
from django.urls import path, include
from administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
]
