from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)

from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(
            request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NbKLRJ7u0o8oEB3CW5MDb3NoW6vzXXb5j4McdEWIEhiN5WNjNZLEgt20hcKeWM8SbVDjQ36nz2pescJpDH530pM00WgOKfpo5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
