from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

class Home(TemplateView):
    """
    Home class is used to direct to a template where the content is present
    """

    template_name = "index.html"

class Welcome(TemplateView):
    """
    Welcome class is used to direct to a template where the content is present
    """
    template_name = 'welcome.html'

class Thanks(TemplateView):
    """
    Thanks class is used to direct to a template where the content is present
    """
    template_name = 'thanks.html'