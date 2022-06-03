
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    username = forms.CharField(
        label='Username',
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 65 characters',
        },
        widget=forms.TextInput(attrs={
            'placeholder': ' Name',
            'class': 'user-register__username',
        }),
        min_length=4, max_length=65,
    )

    password = forms.CharField(
        label='Password',
        error_messages={
            'required': 'This field must not be empty',
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': ' Password',
            'class': 'user-register__password',
        }),
        min_length=4, max_length=65,
    )
