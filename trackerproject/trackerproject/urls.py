from django.contrib import admin
from django.urls import path
from .trackerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', views.LocationList.as_view()),
    path('/health', views.HealthCheck.as_view()), 
]
