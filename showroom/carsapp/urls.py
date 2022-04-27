from django.urls import path
from django.contrib import admin
from . import views

app_name = 'carsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
    path('searchcar/', views.searchcar, name='searchcar'),
    path('searchsr/', views.searchsr, name='searchsr'),
]

