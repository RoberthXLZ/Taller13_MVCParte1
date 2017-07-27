from django import forms

from cliente.models import Factura

class FacturaForm (forms.ModelForm):

    class Meta:
        model = Factura

        fields = [
            'numero_factura',
            'nombre_factura',
            'fecha_maxima',
            'cantidad',
            'estado_factura',
        ]
        labels = {
            'numero_factura': 'Número'.
            'nombre_factura': 'Empresa',
            'fecha_maxima': 'Fecha Máxima',
            'cantidad': 'Cantidad',
            'estado_factura': 'Estado',
        }
        widgets = {
            'numero_factura': forms.TextInput(),
            'nombre_factura': forms.Select(),
            'fecha_maxima': forms.DateInput(),
            'cantidad': forms.NumberInput(),
            'estado_factura': forms.Select(),
        }
