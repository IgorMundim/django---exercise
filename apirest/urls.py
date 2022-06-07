from django.urls import path

from apirest import views

app_name = 'apirest'

urlpatterns = [
    path('restaurant', views.restaurant_api_list),
    path('restaurant/<int:pk>', views.request_api_detail),
    path('menu/<int:pk>', views.menu_api_list),
    path('menu/<int:restaurant_pk>/<int:menu_pk>', views.menu_api_detail)

]
