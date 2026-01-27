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
        ('luz', '💡 Electricidad (kWh)'),
        ('agua', '💧 Agua (m3)'),
        ('gasolina', '⛽ Gasolina (Galones)'),
        ('transporte', '🚌 Transporte Público ($)'),
    ]

    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    tipo_recurso = models.CharField(max_length=20, choices=OPCIONES_RECURSO)
    cantidad = models.FloatField(help_text="Valor del consumo")
    fecha_consumo = models.DateField(default=timezone.now)
    recomendacion_ia = models.TextField(blank=True, null=True) # Aquí guardaremos lo que diga Gemini

    def __str__(self):
        return f"{self.usuario.nombres} - {self.tipo_recurso}: {self.cantidad}"