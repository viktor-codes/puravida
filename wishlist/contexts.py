from django.shortcuts import get_object_or_404
from .models import Wishlist, Product


def wishlist_items(request):
    # Get the product_id from the query parameters
    product_id = request.GET.get('id')

    # Get the currently authenticated user
    user = request.user

    # Initialize an empty queryset for wishlist
    wishlist = Wishlist.objects.none()
    wishlist_count = 0

    if user.is_authenticated and product_id:
        # If the user is authenticated and product_id is present,
        # filter wishlist for the specific product and user
        product = get_object_or_404(Product, id=product_id)
        wishlist = Wishlist.objects.filter(product=product, user=user)
        wishlist_count = wishlist.count()

    # If the user is authenticated, get all wishlist items for the user
    elif user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=user)
        wishlist_count = wishlist.count()
        wishlist_products = wishlist.values_list('product', flat=True)

    context = {
        "wishlist": wishlist,
        "wishlist_count": wishlist_count,
        "wishlist_products": wishlist_products,
    }
    return context
