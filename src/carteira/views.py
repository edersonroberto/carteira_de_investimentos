from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .models import Transacao, Carteira
from .forms import TransacaoForm, TransacaoFormModel, CarteiraFormModel
# transacao = Transacao.objects.get(id=1)


def transacao_detail_page(request, ticker):
	#obj = Transacao.objects.get(id=id) #--> query , database django render it
	print(type(ticker))
	obj = get_object_or_404(Transacao, ticker=ticker)
	template_name = 'transacao_detail.html' 
	context = {"object": obj}
	return render(request, template_name, context)


def carteira_detail_page(request, ticker):
	#print("Django Says: ", request.method, request.path, request.user)
	obj = get_object_or_404(Carteira, ticker=ticker)
	template_name = 'carteira_detail.html' 
	context = {"object": obj}
	return render(request, template_name, context)


@staff_member_required()
@login_required()
def carteira_list_view(request):
	#print("Django Says: ", request.method, request.path, request.user)
	if not request.user.is_authenticated:
		return render(request, "not-a-user.html", {})
	qs = Carteira.objects.all() # -> list of python objects
	template_name = 'carteira_list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


def carteira_create_view(request):
	form = CarteiraFormModel(request.POST or None)
	if form.is_valid():
		form.save()
		form = CarteiraFormModel()
	template_name = 'carteira_create.html'
	context = {'form': form}
	return render(request, template_name, context)


def transacao_list_view(request, ticker):
	queryset = Transacao.objects.filter(ticker=ticker)
	template_name = 'transacao_details_page.html'
	context = {}
	return render(request, template_name, context)


def transacao_create_view(request):
	form = TransacaoFormModel(request.POST or None)
	if form.is_valid():
		form.save()
		form = TransacaoFormModel()
	template_name = 'transacao_create.html'
	context = {'form': form}
	return render(request, template_name, context)


def transacao_retrieve_view(request, ticker):
	obj = get_object_or_404(Transacao, ticker=ticker)
	template_name = 'transacao_retrieve.html' 
	context = {"object": obj}
	return render(request, template_name, context)


@staff_member_required()
def transacao_update_view(request, ticker):
	obj = get_object_or_404(Transacao, ticker=ticker)
	form = TransacaoFormModel(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'transacao_update.html'
	context = {'form': form, "title": f"Update {obj.ticker}"}
	return render(request, template_name, context)

@staff_member_required()
def transacao_delete_view(request, ticker):
	obj = get_object_or_404(Transacao, ticker=ticker)
	template_name = 'transacao_delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/carteira")
	context = {"object": obj}
	return render(request, template_name, context)

