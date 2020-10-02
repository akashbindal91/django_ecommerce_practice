from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    docstring
    """
    first_name = forms.CharField(max_length=254, required=False)
    last_name = forms.CharField(max_length=254, required=False)
    email = forms.EmailField(
        max_length=254, required=True, help_text='eg. youremail@mymail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email' )
