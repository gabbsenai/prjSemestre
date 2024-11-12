from django.views.generic import TemplateView
from django.db.models import Sum, F, Case, When
from django.contrib.auth.mixins import LoginRequiredMixin
from projeto.models import Produto

class ProdutoSaldoView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        produtos = Produto.objects.annotate(
            saldo=Sum(
                Case(
                    When(movimentacao__tipo='E', then=F('movimentacao__quantidade')),
                    When(movimentacao__tipo='S', then=-F('movimentacao__quantidade')),
                    default=0,
                )
            )
        ).order_by('-id')[:10]  

        context['produtos'] = produtos
        return context