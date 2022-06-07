

from functools import partial
from multiprocessing import context

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurant.models import MenuItem, Restaurant
from restaurant.serializers import MenuItemSerializer, RestaurantSerializer

# Create your views here.


@ api_view(http_method_names=['get', 'post'])
def restaurant_api_list(request):
    if request.method == 'GET':
        restaurant = Restaurant.objects.all().order_by('-id')
        serializer = RestaurantSerializer(
            instance=restaurant,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RestaurantSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(http_method_names=['get', 'patch', 'delete'])
def menu_api_detail(request, restaurant_pk, menu_pk):
    menu = get_object_or_404(MenuItem.objects.filter(
        id=menu_pk).all())
    if request.method == 'GET':
        serializer = MenuItemSerializer(
            instance=menu,
            many=False,
            context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = MenuItemSerializer(
            instance=menu,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['get', 'patch', 'delete'])
def request_api_detail(request, pk):

    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'GET':
        serializer = RestaurantSerializer(
            instance=restaurant,
            many=False,
            context={'request': request},
        )
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = RestaurantSerializer(
            instance=restaurant,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['get', 'post'])
def menu_api_list(request, pk):
    if request.method == 'GET':
        menu = MenuItem.objects.filter(restaurant_id=pk).order_by('-id')
        serializer = MenuItemSerializer(
            instance=menu,
            many=True,
            context={'request': request},
        )

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuItemSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
