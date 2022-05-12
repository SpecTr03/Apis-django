from pyexpat import model
from django.db import models


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
    
#
class Hobby(TimeStampedModel):
    hobby = models.CharField('Pasa Tiempo', max_length=50)

    def __str__(self):
        return self.hobby



class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobbies = models.ManyToManyField(Hobby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name


class Reunion(TimeStampedModel):
    persona = models.ForeignKey(
        Person, on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField('asunto de reunion', max_length=100)

    class Meta: 
        verbose_name = 'Reunionm'
        verbose_name_plural = 'Reunions'

    def __str__(self):
        return self.asunto

