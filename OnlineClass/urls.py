
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from users.views import home_redirect_view


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

# def home_view(request):
#     return render(request, 'home.html')

urlpatterns = [
path('admin/', admin.site.urls),
path('', home_redirect_view, name='home'),
path('home/', login_view, name='home'),
path('login/', login_view, name='login'),
path('register/', register_view, name='register'),
]

