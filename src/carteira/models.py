from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Ticker(models.Model):
	#user   = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	ticker = models.SlugField(unique=True)
	nome   = models.CharField(max_length=50)
	setor  = models.CharField(max_length=50)
	tipo   = models.CharField(max_length= 50, default='Ação')

	def __str__(self):
		return self.ticker
	#def get_absolute_url(self):
	#	return f"transacao/{ self.ticker}"


class Transacao(models.Model):
	#ticker = models.SlugField()
	dataCompra = models.DateField()
	valorCompra = models.DecimalField(max_digits=7, decimal_places=2)
	quantidade = models.DecimalField(max_digits=4, decimal_places=0)
	taxa = models.DecimalField(max_digits=5, decimal_places=2)
	dataVenda = models.DateField(null=True, blank=True)
	valorVenda = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
	ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, null=True)

	#def get_edit_url(self):
	#	#print(self)
	#	return "edit/"

	#def get_delete_url(self):
	#	return "delete/"
			

class Dividendos(models.Model):
	#ticker = models.SlugField()
	dataDividendo = models.DateField(null=True, blank=True)
	dataPagamento = models.DateField(null=True, blank=True)
	dividendos 	  = models.DecimalField(max_digits=5, decimal_places=2)
	ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, null=True)
