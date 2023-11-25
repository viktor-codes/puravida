from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


admin.site.register(Wishlist, WishlistAdmin)
