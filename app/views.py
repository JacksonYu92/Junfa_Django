from django.shortcuts import render
from django.template import Template, Context
from django.db.models import Q
from app import models


def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def products(request, pid):
    product = models.Product.objects.filter(id=pid).first()
    # product = models.Product.objects.get(name='Energy Saving Double Low-E Insulating Glass Unit')
    context = {'product': product}
    return render(request, 'products.html', context)

def results(request):
    return render(request, 'results.html')