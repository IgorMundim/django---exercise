from dataclasses import fields

from rest_framework import serializers

from restaurant.models import MenuItem, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = 'id', 'name', 'cover', 'author'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = 'id', 'category', 'name', 'description', 'price', 'cover', 'restaurant'
