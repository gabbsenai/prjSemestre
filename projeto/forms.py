from django import forms
from projeto.models import Categoria, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao',]
        labels = {
            'nome': 'Nome da categoria',
            'descricao': 'Descrição da Categoria',
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valor', 'descricao', 'categoria', 'imagem', 'estado'] 
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição do Produto',
            'valor': 'Valor(R$)',
            'categoria': 'Categoria',
            'imagem': 'Imagem',
            'estado': 'Estado'
        }     
  