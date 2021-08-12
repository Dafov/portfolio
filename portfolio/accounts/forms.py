from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


UserModel = get_user_model()


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your email',
                'label': False,
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'col-md-8 form-control',
                'placeholder': 'Your password',
                'label': False,
            }
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Your email adress',
                'label': False,
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Your password',
                'label': False,
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm password',
                'label': False,
            }
        )
