# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from cliente.models import Factura
from cliente.forms import FacturaForm

# Create your views here.

def index(request):
    facturas = Factura.objects.all()
    contexto = {'facturas':facturas}
    return render(request,'facturas/factura_lista.html',contexto)


def create(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = FacturaForm()
    return render(request, 'facturas/factura_formulario.html',{'form':form})
    
