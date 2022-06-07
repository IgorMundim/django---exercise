from django.urls import path

from restaurant import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('restaurant/edit/<int:id>', views.restaurant_edit, name='restaurant_edit'),  # noqa E501
    path('restaurant/new', views.restaurant_new, name='restaurant_new'),
    path('restaurant/delete/<int:id>', views.restaurant_delete, name='restaurant_delete'),  # noqa E501


    path('menu/<int:id>', views.menu_item, name='menu'),
    path('menu/delete/<int:id>', views.menu_item_delete, name='menu_delete'),
    path('menu/edit/<int:id>', views.menu_item_edit, name='menu_edit'),
]
