from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login — uses Django's built-in LoginView
    # template_name tells it which HTML template to render
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    
    # Logout — uses Django's built-in LogoutView
    # Redirects to LOGOUT_REDIRECT_URL defined in settings.py
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    
    # Registration — our custom view
    path(
        'register/',
        views.register,
        name='register'
    ),
]