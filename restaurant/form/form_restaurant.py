from django import forms
from django.core.exceptions import ValidationError
from restaurant.models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = 'name', 'cover', 'id'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        exists = Restaurant.objects.filter(name=name).exists()

        if exists:
            raise ValidationError(
                'Restaurant name is already in use', code='invalid',
            )
        return name

    name = forms.CharField(
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Name must have at least 4 characters',
            'max_length': 'Name must have less than 65 characters',
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'menu-restaurant__input',
        }),
        min_length=4, max_length=65,
    )
