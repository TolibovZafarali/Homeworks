from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('en/', views.english),
    path('ru/', views.russian),
    path('uz/', views.uzbek),
]