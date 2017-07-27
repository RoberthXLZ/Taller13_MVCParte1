# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Factura

# Create your views here.

def index(request):
    facturas = Factura.objects.all()
    contexto = {'facturas':facturas}
    return render(request,'facturas/factura_lista.html',contexto)

def create(request):
    return HttpResponse("create")
