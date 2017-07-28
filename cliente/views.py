# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from cliente.models import Factura
from cliente.forms import FacturaForm
from django.contrib import messages


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
            messages.add_message(request, messages.SUCCESS, 'Factura creada con exito!')
        return redirect('factura:listar')
    else:
        form = FacturaForm()
        messages.add_message(request, messages.SUCCESS, 'Error al crear Factura!')
    return render(request, 'facturas/factura_formulario.html',{'form':form})


    
def listar(request):
    facturas = Factura.objects.filter(estado_factura='Pendiente')
    return render(request,'facturas/factura_listaPendiente.html',{'facturas':facturas})


def eliminarFactura(request, id):
    factura = Factura.objects.get(id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('factura:index')
    return render(request, 'facturas/factura_eliminar.html', {'facturas': factura})

def editarFactura(request, id):
    factura = Factura.objects.get(id=id)
    if request.method =='GET':
        form = FacturaForm(instance=factura)
    else:
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
        return redirect('factura:index')
    return render(request, 'facturas/factura_formulario.html',{'form':form})

