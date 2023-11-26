from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product
from django.contrib import messages


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.all()
    wishlist_count = Wishlist.objects.count()

    context = {
        "wishlist": wishlist,
        "wishlist_count": wishlist_count,
    }
    return render(request, "wishlist/wishlist.html", context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)

    if created:
        messages.success(
            request, f'{product.name} has been added to your wishlist.')
    else:
        messages.error(request, f'{product.name} is already in your wishlist.')

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_wishlist(request, product_id):
    # Get the product
    product = get_object_or_404(Product, id=product_id)

    # Get the wishlist item for the user and product
    wishlist_item = get_object_or_404(
        Wishlist, user=request.user, product=product)

    # Delete the wishlist item
    wishlist_item.delete()

    messages.success(request, 'Successfully removed product from wishlist.')
    return redirect('wishlist')
