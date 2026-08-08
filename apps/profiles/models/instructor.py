from django.db import models
from django.conf import settings

class InstructorProfile(models.Model):
    """
    Para definir relaciones en tus Modelos (ForeignKey, OneToOneField)Utiliza settings.AUTH_USER_MODEL. Pasar una cadena de texto evita problemas de importación circular cuando los modelos se están cargando al iniciar la aplicación.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    photo = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    social_network = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'Instructor: {self.get_full_name() or self.username}'