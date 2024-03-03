from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
from administration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.index, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
