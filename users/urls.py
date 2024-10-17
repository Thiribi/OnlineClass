from django.urls import path
from .views import RegisterView, LoginView
from django.shortcuts import redirect

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', LoginView.as_view(), name='home'),
]

def home_redirect_view(request):
    return redirect('home')  # Redirect to the login page

