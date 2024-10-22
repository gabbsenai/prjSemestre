from django.contrib import admin
from django.urls import path
from projeto.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    #categoria
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/update/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    #produto
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('produto/create/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/update/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto_delete'),
]