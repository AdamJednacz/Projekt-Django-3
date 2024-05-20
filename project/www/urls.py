from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('clubs/', views.clubs, name='clubs'),   
    path('players/', views.players, name='players'),   
    path('positions/', views.positions, name='positions'),   
]
