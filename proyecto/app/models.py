from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import IntegerField


# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)
    def __unicode__(self):
        return self.titulo
    
class Enlace(models.Model):
    titulo = models.CharField(max_length=140)
    enlace = models.URLField()
    votos  = IntegerField(default=0)
    categorias = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s - %s"% (self.titulo,self.enlace)

    def mis_votos_en_imagen_rosada(self):
        return 'http://placehold.it/200x100/E8117F/ffffff/&text=%d+votos' % self.votos

    def es_popular(self):
        return self.votos >1
    es_popular.boolean = True

class Agregador(models.Model):
    titulo  = models.CharField(max_length=140)
    enlaces = models.ManyToManyField(Enlace)

if __name__ == '__main__':
    print "holi"