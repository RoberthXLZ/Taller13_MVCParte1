# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Factura (models.Model):
	numero_factura = models.CharField(max_length=16)
	AGUA = 'Agua'	
	LUZ = 'Luz'
	TELEFONO = 'Telefono'
	FACTURA_OPCIONES = (
		(AGUA, 'Agua'),
		(LUZ, 'Luz'),
		(TELEFONO, 'Telefono'),
	)
	nombre_factura = models.CharField(max_length=8,choices=FACTURA_OPCIONES,default=AGUA)
	fecha_maxima = models.DateField()
	cantidad = models.DecimalField(max_digits = 8, decimal_places = 2)
	PAGADO = 'Pagado'	
	PENDIENTE = 'Pendiente'
	ACUMULADO = 'Acumulado'
	ESTADO_OPCIONES = (
		(PAGADO, 'Pagado'),
		(PENDIENTE, 'Pendiente'),
		(ACUMULADO, 'Acumulado'),
	)
	estado_factura = models.CharField(max_length=11,choices=ESTADO_OPCIONES,default='Pagado')
	

class Recibo (models.Model):
        numero_recibo = models.CharField(max_length=16)
        echa_pago = models.DateField()
        nombre_de_quien_recibe = models.CharField(max_length=30)
        AGUA = 'Agua'
        LUZ = 'Luz'
        TELEFONO = 'Telefono'
        FACTURA_OPCIONES = (
                (AGUA, 'Agua'),
                (LUZ, 'Luz'),
                (TELEFONO, 'Telefono'),
        )
        concepto_recibo = models.CharField(max_length=8,choices=FACTURA_OPCIONES,default=AGUA)
        cantidad = models.DecimalField(max_digits = 8, decimal_places = 2)
