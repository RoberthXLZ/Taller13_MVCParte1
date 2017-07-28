from django.conf.urls import include, url

from cliente.views import create, index, eliminarFactura,editarFactura
app_name = 'factura'

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^create$', create, name = 'create'),
    url(r'^editar/(?P<id>\d+)$', editarFactura, name='editarFactura'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarFactura, name='eliminarFactura'),

    
]
