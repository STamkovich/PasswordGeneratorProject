from django.urls import path
from . import views


urlpatterns = [
    path('password/', views.get_password, name='password'),
    path('info', views.info, name='info')
]
