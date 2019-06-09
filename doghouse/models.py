from django.db import models

class Animal(models.Model):
    TIPO_CHOICES = (
        ('C', 'Cachorro'), 
        ('G', 'Gato')
    )
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)    
    tipo_animal = models.CharField(choices=TIPO_CHOICES, max_length=1, default='C')
    raca = models.CharField(max_length=30)
    cor_pelos = models.CharField(max_length=30)
    cor_olhos = models.CharField(max_length=30)
    tipo_pelagem = models.CharField(max_length=30)
    data_nascimento = models.DateField(null=True, blank=True)
    data_resgate = models.DateField()
    adotado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos_animais', null=True, blank=True)

    def __str__(self):
        return self.nome
