from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username",)
