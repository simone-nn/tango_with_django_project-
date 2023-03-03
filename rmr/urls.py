from django.urls import path
from rmr import views

app_name = 'rmr'

urlpatterns = [
    path('', views.index, name='index'),
]