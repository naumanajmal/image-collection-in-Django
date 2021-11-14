
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name = 'index'),
    path('register',  views.register, name = 'register'),
    path('login',  views.logindef, name = 'login'),
    path('logout',  views.logoutdef, name = 'logout'),
    path('images',  views.images, name = 'images'),
]
