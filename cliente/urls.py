from django.conf.urls import include, url

from cliente.views import create, index, eliminarFactura,editarFactura,listar,createRecibo,eliminarRecibo,
app_name = 'factura'

urlpatterns = [
    url(r'^$', index_general, name = 'index'),
    url(r'^createRecibo$',createRecibo, name = 'createRecibo'),
    url(r'^create$', create, name = 'create'),
    url(r'^editar/(?P<id>\d+)$', editarFactura, name='editarFactura'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarFactura, name='eliminarFactura'),
    url(r'^eliminar/(?P<id>\d+)$', eliminarRecibo, name='eliminarRecibo'),
   
]
