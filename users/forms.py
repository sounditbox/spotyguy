from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, PasswordInput


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



