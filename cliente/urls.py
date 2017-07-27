from django.conf.urls import include, url

from cliente.views import create, index

urlpatterns = [
    url(r'^', index),
    url(r'^create/', create),
    
]
