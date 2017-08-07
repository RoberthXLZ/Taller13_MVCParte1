from django.shortcuts import render
from cliente.models import Factura,Recibo
from cliente.serializers import FacturaSerializer,ReciboSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ReciboViewSet(ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer
