from django.shortcuts import render
from newsletter.forms import SubscibersForm


def index(request):
    context = {
        'form': SubscibersForm(),
    }
    return render(request, 'home/index.html', context)


def custom_404(request, exception):
    return render(request, 'home/error/404.html', status=404)
