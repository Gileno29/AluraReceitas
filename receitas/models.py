from distutils.command.upload import upload
from pyexpat import model

from django.db import models
from datetime import datetime

from pessoas.models import Pessoa

# Create your models here.
class Receita(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita=models.CharField(max_length=200)
    ingredientes=models.TextField()
    modo_prearo=models.TextField()
    tempo_preparo=models.IntegerField()
    rendimento= models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)
    data_receita= models.DateTimeField(default=datetime.now, blank=True)
    publicada= models.BooleanField(default=False)
    foto_receita= models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_receita
