from django import forms
from .models import Transacao, Carteira

class TransacaoForm(forms.Form):
	ticker = forms.SlugField()
	dataCompra = forms.DateField()
	valorCompra = forms.DecimalField()
	quantidade = forms.IntegerField()
	taxa = forms.DecimalField()
	dataVenda = forms.DateField(required=False)
	valorVenda = forms.DecimalField(required=False)


class TransacaoFormModel(forms.ModelForm):
	class Meta:
		model = Transacao
		fields = ['ticker', 'dataCompra', 'valorCompra', 'quantidade', 'taxa', 'dataVenda', 'valorVenda']
	

class CarteiraFormModel(forms.ModelForm):
	class Meta:
		model = Carteira
		fields = ['ticker', 'nome', 'setor', 'tipo']

	def clean_ticker(self, *args, **kwargs):
		instance = self.instance
		print(instance)
		ticker = self.cleaned_data.get('ticker')
		qs = Transacao.objects.filter(ticker__iexact=ticker)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError("This ticker is already been use")
		return ticker