from django.contrib import admin

# Register your models here.
from .models import Transacao, Ticker

admin.site.register(Transacao)
admin.site.register(Ticker)