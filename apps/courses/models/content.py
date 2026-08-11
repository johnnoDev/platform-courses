from .module import Module
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Herencia/Interfaz Abstracta - Tabla Abstracta
class ItemBase(models.Model):
    """
    %(class)s es un placeholder que evita colisiones de nombres en el modelo relacionado (User) cuando varias subclases heredan el mismo campo de una clase base abstracta. Sin este truco, tu proyecto simplemente no arrancaría por el conflicto de related_name duplicado.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_related'
    )
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    content = models.FileField(upload_to='files')

class Image(ItemBase):
    content = models.FileField(upload_to='images')

class Video(ItemBase):
    content = models.URLField()

class Content(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='contents'
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, limit_choices_to={
            'text', 'image', 'video', 'file'
        }
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')