from django.shortcuts import render
from .models import Production


def production(request):
    return render(request, 'production/production_html.html')
