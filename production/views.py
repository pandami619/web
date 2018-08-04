from django.shortcuts import render
from .models import *


def product(request, product_id):
    product = Production.objects.get(id=product_id)
    print(product, 'id')

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key, 'request session key')

    return render(request, 'production/only_one_production.html', locals())


def production(request):
    productions_image = ProductionImage.objects.filter(is_active=True, is_main=True, product_is_active=True)
    return render(request, 'production/production_html.html', locals())
