from django.shortcuts import render
from accounts.forms import UserForm
from accounts.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
    """
    This class is used for Creating view for Sign Up form
    """

    model = User
    form_class = UserForm
    template_name = "accounts/SignUp.html"
    success_url = reverse_lazy("login")

