from django.contrib.auth.forms import AuthenticationForm
from django import forms


# Simple form for user login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Needed to add bootstrap classes to the LoginView
class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'my-username-class'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'my-password-class'}
        )