from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    estado = models.CharField(max_length=1, choices=[('N', 'Novo'), ('U', 'Usado')])
    imagem = models.ImageField(upload_to='produto/', null=True, blank=True)

    def __str__(self):
        return self.nome