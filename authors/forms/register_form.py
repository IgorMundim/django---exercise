
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    first_name = forms.CharField(
        label='First Name',
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 65 characters',
        },
        widget=forms.TextInput(attrs={
            'placeholder': ' First Name',
            'class': 'user-register__firstname',
        }),
        min_length=4, max_length=65,
    )
    last_name = forms.CharField(
        label='Last Name',
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 65 characters',
        },
        widget=forms.TextInput(attrs={
            'placeholder': ' Last Name',
            'class': 'user-register__lastname',
        }),
        min_length=4, max_length=65,
    )
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
    email = forms.CharField(
        label='Username',
        error_messages={
            'required': 'This field must not be empty',

        },
        widget=forms.TextInput(attrs={
            'placeholder': ' Email',
            'class': 'user-register__email',
        }),
        min_length=4, max_length=150,
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

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )
        return email
