from portfolio.contact.forms import MessageForm
from portfolio.contact.models import Message
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView

# Create your views here.


class CreateMessageView(FormView):
    template_name = 'contact.html'
    form_class = MessageForm
    success_url = '../'

    def form_valid(self, form):
        message = form.save(commit=False)
        message.save()
        return super().form_valid(form)


class InboxPageView(ListView):
    model = Message
    template_name = 'inbox.html'
    context_object_name = 'inbox'


    def get_queryset(self):
        inbox = Message.objects.all().order_by('-created')
        inbox.order_by('is_read')
        return inbox


class MessageDetailView(DetailView):
    template_name = "message.html"
    context_object_name = "message"

    def get_object(self):
        id_ = self.kwargs.get("id")
        message = get_object_or_404(Message, id=id_)
        message.is_read = True
        message.save()
        return message