from django.urls import path

from authors import views

app_name = 'authors'

urlpatterns = [
    path('', views.register_view, name='register'),  # Home
    path('create/', views.register_create, name='register_create'),
    path('login/', views.login, name='login'),
]
