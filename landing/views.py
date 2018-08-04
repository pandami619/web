from django.shortcuts import render
from .forms import SubscriberForm
from production.models import *


def landing(request):
    name = "test"
    current_day = "2018"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, '', locals())


def home(request):
    products_images = ProductionImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, '../production/templates/production/production_html.html', locals())