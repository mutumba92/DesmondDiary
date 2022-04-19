from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newNote/<str:pk>', views.newNote, name='newNote')
]
