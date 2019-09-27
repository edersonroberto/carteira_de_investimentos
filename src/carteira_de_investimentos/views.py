from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
	my_title = "hello there ..."
	context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
	return render(request, "home.html", context)


def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {"title": "contact us", "form": form}
	return render(request, "form.html", context)



