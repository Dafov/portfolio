from django.forms import ModelForm
from portfolio.contact.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']
        

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
             {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your name',
                'label': False,
                'type':'text'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your email',
                'label': False,
                'type':'email'
            }
        )
        self.fields['subject'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Subject',
                'label': False,
                'type':'subject'
            }
        )
        self.fields['body'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Message',
                'label': False,
                'type':'message'
            }
        )

