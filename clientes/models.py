from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    SEXO = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outros', 'Outros'),
    )
    sexo = models.CharField(max_length=30, choices=SEXO, null=True, blank=True)
    salario = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='clientes_photo', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
