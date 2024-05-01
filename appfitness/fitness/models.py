from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='canciones/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Playlist(models.Model):
    
    nombre = models.CharField(max_length=200)
    q1 = models.OneToOneField(Cancion, related_name='q1', null=True, blank=True, on_delete=models.SET_NULL)
    q2 = models.OneToOneField(Cancion, related_name='q2', null=True, blank=True, on_delete=models.SET_NULL)
    q3 = models.OneToOneField(Cancion, related_name='q3', null=True, blank=True, on_delete=models.SET_NULL)
    q4 = models.OneToOneField(Cancion, related_name='q4', null=True, blank=True, on_delete=models.SET_NULL)
    recharge = models.OneToOneField(Cancion, related_name='recharge', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre

