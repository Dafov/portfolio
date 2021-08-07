from django.views.generic.base import TemplateView
from portfolio.contact.models import Message
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class ContactTempalteView(TemplateView):
    template_name = 'contact.html'


# class InboxPageView(ListView):
#     messages = Message.objects.all().order_by('is_read')
#     unread_count = Message.objects.filter(is_read=False).count()
#     context_object_name = 'messages', 'unread_count'
#     template_name = 'inbox.html'


def inbox_page(request):
    inbox = Message.objects.all().order_by('is_read')
    unread_count = Message.objects.filter(is_read=False).count()

    context = {
        'inbox': inbox,
        'unread_count': unread_count
        }
    
    return render(request, 'inbox.html', context)