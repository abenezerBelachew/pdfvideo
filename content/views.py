from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Content

class HomePageView(ListView):
    model = Content
    template_name = 'home.html'
    context_object_name = 'contents'
    