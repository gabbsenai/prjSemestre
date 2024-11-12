from movimentacao.models import Movimentacao
from projeto import forms


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto','quantidade', 'tipo']