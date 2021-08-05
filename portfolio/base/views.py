# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


# def home_page(request):
#     return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'