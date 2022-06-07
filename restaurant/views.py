from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from restaurant.form.form_restaurant import RestaurantForm
from restaurant.form.from_menu import MenuForm
from restaurant.models import MenuItem, Restaurant


def home(request):
    restaurants = Restaurant.objects.all().order_by('-id')
    form = RestaurantForm()
    return render(request, 'restaurant/pages/home.html',
                  context={'restaurants': restaurants, 'form': form
                           # noqa E501
                           })


def restaurant_new(request):
    if not request.POST:
        raise Http404()
    form = RestaurantForm(request.POST, request.FILES)

    if form.is_valid():
        print(form)
        # restaurant = Restaurant(
        #     name=request.POST['name'], cover=request.FILES['cover'])
        # restaurant.save()
        form.save()

    return redirect(reverse('restaurant:home'))


def restaurant_edit(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)

    if request.POST:
        form = RestaurantForm(request.POST, request.FILES)

        if form.is_valid():
            restaurant_temp = form.save(commit=False)
            restaurant_temp.id = restaurant.id
            restaurant_temp.save()
            return redirect(reverse('restaurant:home'))
    return render(request, 'restaurant/pages/restaurant_edit.html',
                  context={'restaurant': restaurant,
                           })


def restaurant_delete(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    restaurant.delete()
    return redirect(reverse('restaurant:home'))


def menu_item(request, id):

    menu_itens = MenuItem.objects.filter(restaurant_id=id).order_by('-id')
    if request.POST:
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant = get_object_or_404(Restaurant, pk=id)
            menu_item.save()
    return render(request, 'restaurant/pages/menu_item.html', context={
        'menu_itens': menu_itens,
        'restaurant_id': id,
    })


def menu_item_edit(request, id):

    if request.POST:
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            search = get_object_or_404(MenuItem, pk=id)
            menu_item = form.save(commit=False)
            menu_item.restaurant_id = search.restaurant_id
            menu_item.id = id
            menu_item.save()
            menu_itens = MenuItem.objects.filter(
                restaurant_id=search.restaurant_id).order_by('-id')
            return render(request, 'restaurant/pages/menu_item.html', context={
                'menu_itens': menu_itens,
                'restaurant_id': search.restaurant_id,
            })
    menu_itens = get_object_or_404(MenuItem, pk=id)
    return render(request, 'restaurant/pages/menu_item_edit.html', context={
        'menu_item': menu_itens,
    })


def menu_item_delete(request, id):
    menu_item = get_object_or_404(MenuItem, pk=id)
    redirect_id = menu_item.restaurant_id
    menu_item.delete()

    menu_itens = MenuItem.objects.filter(
        restaurant_id=redirect_id).order_by('-id')
    return render(request, 'restaurant/pages/menu_item.html', context={
        'menu_itens': menu_itens,
        'restaurant_id': redirect_id,
    })
