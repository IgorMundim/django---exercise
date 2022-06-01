from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'restaurant/pages/home.html')


def menu_item(request):
    return render(request, 'restaurant/pages/menu_item.html')


def menu_item_edit(request):
    return render(request, 'restaurant/pages/menu_item_edit.html')


def restaurant_edit(request):
    return render(request, 'restaurant/pages/restaurant_edit.html')
