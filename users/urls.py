from django.urls import path
from .views import RegisterView, LoginView
from django.shortcuts import redirect
from .views import register
from .views import login

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', LoginView.as_view(), name='home'),
    path('register/', register, name='register'),  # Registration API endpoint
    path('login/', login, name='login'),  # Login API endpoint
]

def home_redirect_view(request):
    return redirect('home')  # Redirect to the login page
