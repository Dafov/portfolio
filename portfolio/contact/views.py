from portfolio.common.superuser_mixins import SuperUserRequiredMixin
from portfolio.contact.forms import MessageForm
from portfolio.contact.models import Message
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.urls.base import reverse_lazy

# Create your views here.
class InboxPageView(SuperUserRequiredMixin, ListView):
    model = Message
    template_name = 'contacts/inbox.html'
    context_object_name = 'inbox'

    def get_queryset(self):
        inbox = Message.objects.all().order_by('-created')
        return inbox

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_super"] = self.request.user.is_superuser
        return super().get_context_data(**kwargs)


class MessageDetailView(SuperUserRequiredMixin, DetailView):
    template_name = "contacts/message.html"
    context_object_name = "message"

    def get_object(self):
        id_ = self.kwargs.get("id")
        message = get_object_or_404(Message, id=id_)
        message.is_read = True
        message.save()
        return message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_super"] = self.request.user.is_superuser
        return super().get_context_data(**kwargs)


class CreateMessageView(FormView):
    template_name = 'contacts/contact.html'
    form_class = MessageForm
    success_url = reverse_lazy('hero')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.save()
        return super().form_valid(form)

class DeleteMessageView(SuperUserRequiredMixin, DeleteView):
    template_name = 'contacts/message_delete.html'
    model = Message
    success_url = reverse_lazy('inbox')