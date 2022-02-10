from django.contrib import admin
from django.urls import path, include
from app_1.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_1.urls')),
    path('', HomeView.as_view(), name='login'),
]
