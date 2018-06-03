from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Production


urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Production.objects.all(),
     template_name="production/production_html.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Production,
    template_name="production/only_one_production.html")),
]
#url(r'^$', views.production, name='production')
