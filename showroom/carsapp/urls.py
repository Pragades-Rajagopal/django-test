from django.urls import path
from . import views

app_name = 'carsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
    path('searchcar/', views.searchcar, name='searchcar'),
    path('searchsr/', views.searchsr, name='searchsr'),
    path('addcar/', views.addcar, name='addcar'),
    path('postcar/', views.postcar, name='postcar'),
]

