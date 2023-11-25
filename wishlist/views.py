from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wishlist


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.all()
    wishlist_count = Wishlist.objects.count()

    context = {
        "wishlist": wishlist,
        "wishlist_count": wishlist_count,
    }
    return render(request, "wishlist/wishlist.html", context)
