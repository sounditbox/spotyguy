from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class LoginForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(),
            'password': PasswordInput()
        }
        labels = {
            'username': 'Username',
            'password': 'Password'
        }


class RegisterForm(ModelForm):
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        widgets = {
            'username': TextInput(),
            'email': EmailInput(),
            'password': PasswordInput(),
        }
        labels = {
            'username': 'Nickname',
            'email': 'E-mail',
            'password': 'Password',
            'password2': 'Repeat password',

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError("Passwords do not match!")
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if get_user_model().objects.filter(email=cd['email']).exists():
            raise ValidationError('User with this email already exists!')
        return cd['email']