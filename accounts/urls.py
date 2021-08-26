from django.urls import path 
from django.contrib.auth import views as auth_views
from accounts import views
from accounts.forms import UserLoginForm


app_name = 'accounts'

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html",authentication_form=UserLoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]