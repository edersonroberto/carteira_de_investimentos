from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, FloatField, F
# Create your views here.
from .models import Transacao, Ticker, Dividendos
from .forms import TransacaoFormModel, TickerFormModel, DividendoFormModel #TransacaoForm,
# transacao = Transacao.objects.get(id=1)
import requests


KEY = '218a7497'

@staff_member_required()
@login_required()
def carteira_list_view(request):
	#print("Django Says: ", request.method, request.path, request.user)
	if not request.user.is_authenticated:
		return render(request, "not-a-user.html", {})
	#qs = Transacao.objects.all() # -> list of python objects
	qs = Transacao.objects.values('ticker__ticker', 'ticker__nome', 'ticker__setor', 'ticker__tipo').annotate(
		Sum('quantidade'), preco_medio=Sum(F('valorCompra') * F('quantidade'))  / Sum(F('quantidade'))
		,total_taxa=Sum('taxa'), total_pago=Sum((F('valorCompra') * F('quantidade')) + F('taxa')))
	print(str(qs.query))
	template_name = 'carteira_list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


def carteira_create_view(request):
	form = TickerFormModel(request.POST or None)
	if form.is_valid():
		form.save()
		form = TickerFormModel()
	template_name = 'carteira_create.html'
	context = {'form': form}
	return render(request, template_name, context)


def carteira_update_view(request, ticker):
	#print("Django Says: ", request.method, request.path, request.user)
	obj = get_object_or_404(Ticker, ticker=ticker)
	template_name = 'carteira_update.html' 
	context = {"object": obj}
	return render(request, template_name, context)


@staff_member_required()
def carteira_delete_view(request, id):
	obj = get_object_or_404(Ticker, id=id)
	template_name = 'carteira_delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/carteira")
	context = {"object": obj}
	return render(request, template_name, context)


def transacao_detail_page(request, ticker):
	#obj = Transacao.objects.get(id=id) #--> query , database django render it
	codigo_ticker = Ticker.objects.get(ticker=ticker)
	#print(type(codigo_ticker))
	rqt = 'https://api.hgbrasil.com/finance/stock_price?key='+KEY+'&symbol='+ticker
	response = requests.get(rqt)
	acao = response.json()
	print(acao.get('results').get(ticker).get('price'))
	#obj = get_object_or_404(Transacao, ticker=codigo_ticker.id)
	qs = Transacao.objects.all().filter(ticker=codigo_ticker.id).annotate(total_pago=Sum('quantidade') * Sum('valorCompra') + ('taxa'))

	template_name = 'transacao_detail.html' 
	context = {"object_list": qs, "price": acao.get('results').get(ticker).get('price')}
	return render(request, template_name, context)


def transacao_list_view(request):
	#print("Django Says: ", request.method, request.path, request.user)
	#if not request.user.is_authenticated:
	#	return render(request, "not-a-user.html", {})
	qs = Transacao.objects.all().order_by('dataCompra') # -> list of python objects
	#print(qs[0].carteira.id)
	template_name = 'transacoes_list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

def ticker_list_view(request):
	#print("Django Says: ", request.method, request.path, request.user)
	#if not request.user.is_authenticated:
	#	return render(request, "not-a-user.html", {})
	qs = Ticker.objects.all().order_by('ticker') # -> list of python objects
	#print(qs[0].carteira.id)
	template_name = 'ticker_list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

def ticker_delete_view(request, id):
	obj = get_object_or_404(Ticker, id=id)
	template_name = 'ticker_delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/carteira")
	context = {"object": obj}
	return render(request, template_name, context)


'''
def transacao_list_view(request, ticker):
	queryset = Transacao.objects.filter(ticker=ticker)
	template_name = 'transacao_details_page.html'
	context = {}
	return render(request, template_name, context)
'''

def transacao_create_view(request):
	form = TransacaoFormModel(request.POST or None)
	if form.is_valid():
		form.save()
		form = TransacaoFormModel()
	template_name = 'transacao_create.html'
	context = {'form': form}
	return render(request, template_name, context)

'''
def transacao_retrieve_view(request, ticker):
	obj = get_object_or_404(Transacao, ticker=ticker)
	template_name = 'transacao_retrieve.html' 
	context = {"object": obj}
	return render(request, template_name, context)
'''

@staff_member_required()
def transacao_update_view(request, id):
	obj = get_object_or_404(Transacao, id=id)
	form = TransacaoFormModel(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("/carteira/transacao_list/")
	template_name = 'transacao_update.html'
	context = {'form': form, "title": f"Update {obj.ticker}"}
	return render(request, template_name, context)

@staff_member_required()
def transacao_delete_view(request, id):
	obj = get_object_or_404(Transacao, id=id)
	template_name = 'transacao_delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/carteira")
	context = {"object": obj}
	return render(request, template_name, context)


def dividendos_list_view(request):
	qs = Dividendos.objects.all()
	print(qs[0].dataDividendo)
	template_name = 'dividendos_list.html'
	context = {"objtect_list": qs}
	return render(request, template_name, context)


def dividendo_create_view(request):
	form = DividendoFormModel(request.POST or None)
	if form.is_valid():
		form.save()
		form = DividendoFormModel()
	template_name = 'dividendo_create.html'
	context = {'form': form}
	return render(request, template_name, context)

