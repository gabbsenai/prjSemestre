from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from projeto.models import Categoria, Produto
from projeto.forms import CategoriaForm, ProdutoForm


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(CategoriaCreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(CategoriaCreateView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(ProdutoCreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(ProdutoCreateView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
