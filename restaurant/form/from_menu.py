
from django import forms
from django.shortcuts import get_object_or_404
from restaurant.models import MenuItem, Restaurant


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = 'category', 'name', 'description', 'price', 'cover'  # noqa E501

    def clean_restaurant(self):
        restaurant_id = self.cheaned_data.get('restaurant')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        return restaurant
