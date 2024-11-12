from django.urls import path
from homepage.views import ProdutoSaldoView

urlpatterns = [
    path('', ProdutoSaldoView.as_view(), name='homepage'),
]
