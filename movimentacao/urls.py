
from django.urls import path
from movimentacao.views import MovimentacaoCreateView, MovimentacaoDeleteView, MovimentacaoListView, MovimentacaoUpdateView

urlpatterns = [
    path('movimentacao/', MovimentacaoListView.as_view(), name='movimentacao_list'),
    path('movimentacao/nova/', MovimentacaoCreateView.as_view(), name='movimentacao_create'),
    path('movimentacao/<int:pk>/editar/', MovimentacaoUpdateView.as_view(), name='movimentacao_update'),
    path('movimentacao/<int:pk>/excluir/', MovimentacaoDeleteView.as_view(), name='movimentacao_delete'),
]
