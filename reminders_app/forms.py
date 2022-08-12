from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import Events


# Needed to add bootstrap classes to the LoginView
# TODO: Add bootstrap classes
class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'my-username-class'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'my-password-class'}
        )


class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'description', 'date', 'time']
