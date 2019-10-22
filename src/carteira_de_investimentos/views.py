from alpha_vantage.timeseries import TimeSeries
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
import requests

def home_page(request):
	#key = 'EXB25F9U85P4H2OT'
	#ts = TimeSeries(key)
	#aapl, meta = ts.get_daily(symbol='AAPL')
	response = requests.get('https://api.hgbrasil.com/finance/stock_price?key=218a7497&symbol=BIDI4')
	acao = response.json()
	result = acao['results']
	print(type(result))
	print(result.get('BIDI4').get('symbol'))
	#print(meta)
	#print(aapl['2019-10-14'])

	'''
	context = {"title": "Home_page"}
	return render(request, "home.html", context)
	'''
	
	
	return render(request, "home.html", {
		'symbol': result.get('BIDI4').get('symbol'),
		'price': result.get('BIDI4').get('price')
		})
	


def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {"title": "contact us", "form": form}
	return render(request, "form.html", context)



