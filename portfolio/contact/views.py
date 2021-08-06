from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class ContactView(TemplateView):
    template_name = 'contact.html'