from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Photo

urlpatterns = [
     url(r'^$', ListView.as_view(queryset = Photo.objects.all(),
     template_name="about/about_html.html")),
]
