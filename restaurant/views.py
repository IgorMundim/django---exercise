from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from restaurant.models import Restaurant


def home(request):
    restaurants = Restaurant.objects.all().order_by('-id')
    return render(request, 'restaurant/pages/home.html',
                  context={'restaurants': restaurants,
                           'action_menu': reverse('restaurant:menu'),
                           'action_edit': reverse('restaurant:restaurant_edit'),  # noqa E501
                           'action_delete': reverse('restaurant:restaurant_delete'),  # noqa E501
                           })


def restaurant_new(request):
    if not request.POST:
        raise Http404()
    return render(request, 'restaurant/pages/menu_item.html')


def restaurant_edit(request):
    return render(request, 'restaurant/pages/restaurant_edit.html')


def restaurant_delete(request):
    if not request.POST:
        raise Http404()
    return render(request, 'restaurant/pages/menu_item.html')


def menu_item(request):
    return render(request, 'restaurant/pages/menu_item.html')


def menu_item_edit(request):
    return render(request, 'restaurant/pages/menu_item_edit.html')
