from django.forms import ModelForm
from portfolio.contact.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'body': '',
        }
        

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Your name',
                'label': False,
            })
        # self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })
        # self.fields['subject'].label = ''
        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control', })
        # self.fields['body'].label = ''
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })

    def form_valid(self, form):
   
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def success_url(self):
        pass