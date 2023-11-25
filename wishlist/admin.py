from django.contrib import admin
from .models import Wishlist


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


admin.site.register(Wishlist, wishlistAdmin)
