from django.urls import path

from restaurant import views

urlpatterns = [
    path('', views.home),  # Home
    path('menu/', views.menu_item),
    path('menu/edit', views.menu_item_edit),
    path('restaurant/edit', views.restaurant_edit),
]
