from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


UserModel = get_user_model()


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your email',
            }
        )
        self.fields['password'].label = ''
        self.fields['password'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your password',
            }
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Enter email adress',
            }
        )
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Enter password',
            }
        )
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Confirm password',
            }
        )
