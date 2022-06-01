from django.contrib import admin

from .models import MenuItem, Restaurant


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']


admin.site.register(Restaurant, CategoryAdmin)
