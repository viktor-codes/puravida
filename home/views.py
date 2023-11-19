from django.shortcuts import render
from newsletter.forms import SubscibersForm


def index(request):
    context = {
        'form': SubscibersForm(),
    }
    return render(request, 'home/index.html', context)
