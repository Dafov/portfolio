from django.views.generic.base import TemplateView
from portfolio.contact.models import Message
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class ContactTempalteView(TemplateView):
    template_name = 'contact.html'


# class InboxPageView(ListView):
#     model = Message
#     unread_count = Message.objects.filter(is_read=False).count()
#     context_object_name = 'inbox', 'unread_count'
#     template_name = 'inbox.html'

#     def get_queryset(self) :
#         queryset = Message.objects.all().order_by('is_read')
#         return queryset
    
#     def get_context_data(self, **kwargs):
#         context = super(InboxPageView, self).get_context_data(**kwargs)
#         context['inbox'] = self.object



def inbox_page(request):
    inbox = Message.objects.all().order_by('is_read')
    unread_count = Message.objects.filter(is_read=False).count()

    context = {
        'inbox': inbox,
        'unread_count': unread_count
    }

    return render(request, 'inbox.html', context)
