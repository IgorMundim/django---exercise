from django.urls import path

from restaurant import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('menu/', views.menu_item, name='menu'),
    path('menu/edit', views.menu_item_edit),
    path('restaurant/edit', views.restaurant_edit, name='restaurant_edit'),
    path('restaurant/new', views.restaurant_new, name='restaurant_delete'),
    path('restaurant/delete', views.restaurant_delete, name='restaurant_delete'),  # noqa E501

]
