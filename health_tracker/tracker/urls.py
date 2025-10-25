from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_logs, name='health_logs'),
]
