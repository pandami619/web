from django.shortcuts import render
from .models import Novelties, Logo


def main(request):
    return render(request, 'main/main_html.html')
