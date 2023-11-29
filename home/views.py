from django.shortcuts import render
from newsletter.forms import SubscibersForm
from products.models import Product


def index(request):

    products = Product.objects.all()
    
    context = {
        'form': SubscibersForm(),
        'products': products,
    }
    return render(request, 'home/index.html', context)


def custom_404(request, exception):
    return render(request, 'home/error/404.html', status=404)
