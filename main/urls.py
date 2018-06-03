from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Novelties

urlpatterns = [
        url(r'^$', ListView.as_view(queryset = Novelties.objects.all(),
         template_name="main/main_html.html")),
         url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Novelties,
         template_name="main/novelties_html.html")),
]
