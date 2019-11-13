from django.urls import path
from .views import register, profile, change_password
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/change-password', change_password, name='change-password')
]