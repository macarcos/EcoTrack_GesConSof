from django import forms
from .models import RegistroConsumo

class ConsumoForm(forms.ModelForm):
    # Agregamos 'form-control-sm' para que sean más pequeños
    cedula_usuario = forms.CharField(max_length=10, label="Cédula", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ej: 0991234567'}))
    nombre_usuario = forms.CharField(max_length=100, label="Nombres", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ej: Marcos Salazar'}))

    class Meta:
        model = RegistroConsumo
        fields = ['tipo_recurso', 'cantidad', 'fecha_consumo']
        widgets = {
            # Agregamos 'form-control-sm' y 'form-select-sm' aquí también
            'fecha_consumo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}),
            'tipo_recurso': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ej: 150'}),
        }