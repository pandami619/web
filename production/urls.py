from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import *
from production import views


urlpatterns = [
    # url(r'^$', views.production, name='production'),
    url(r'^$', ListView.as_view(queryset=ProductionImage.objects.all(),
                                template_name='production/production_html.html')),
    url(r'^(?P<product_id>\w+)$', views.product, name='product'),
    # url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Production,
    #                                         template_name="production/only_one_production.html")),
]
