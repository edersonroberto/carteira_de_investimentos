from django import forms
from .models import Transacao, Ticker, Dividendos

'''
class TransacaoForm(forms.Form):
	ticker = forms.SlugField()
	dataCompra = forms.DateField()
	valorCompra = forms.DecimalField()
	quantidade = forms.IntegerField()
	taxa = forms.DecimalField()
	dataVenda = forms.DateField(required=False)
	valorVenda = forms.DecimalField(required=False)
'''


class TransacaoFormModel(forms.ModelForm):
	class Meta:
		model = Transacao
		fields = ['ticker', 'dataCompra', 'valorCompra', 'quantidade', 'taxa', 'dataVenda', 'valorVenda']
		#exclude = ['ticker']
		#fields = '__all__'
		
class TickerFormModel(forms.ModelForm):
	class Meta:
		model = Ticker
		fields = ['ticker', 'nome', 'setor', 'tipo']


class DividendoFormModel(forms.ModelForm):
	class Meta:
		model = Dividendos
		fields = ['ticker', 'dataDividendo', 'dataPagamento', 'dividendos']


	'''
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
	'''	