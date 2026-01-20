from django.db import models
from django.utils import timezone

# Modelo para el Usuario (Cumple con "Organización de código")
class PerfilUsuario(models.Model):
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    nombres = models.CharField(max_length=100, verbose_name="Nombres Completos")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    # Fecha de creación para saber la antigüedad del usuario
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} ({self.cedula})"

# Modelo para los Consumos (Aquí es donde se aplica la lógica del negocio)
class RegistroConsumo(models.Model):
    OPCIONES_RECURSO = [
        ('luz', 'Electricidad (kWh)'),
        ('agua', 'Agua (m3)'),
        ('transporte', 'Transporte (km)'),
    ]

    # Relación: Un consumo pertenece a un usuario
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    tipo_recurso = models.CharField(max_length=20, choices=OPCIONES_RECURSO)
    cantidad = models.FloatField(help_text="Valor del consumo")
    
    # Fecha manual o automática para poder comparar "mes a mes"
    fecha_consumo = models.DateField(default=timezone.now)
    
    # Campo para guardar lo que diga la IA (Gemini) en el futuro
    recomendacion_ia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_recurso}: {self.cantidad} - {self.fecha_consumo}"