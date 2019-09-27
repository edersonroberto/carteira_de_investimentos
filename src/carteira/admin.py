from django.contrib import admin

# Register your models here.
from .models import Transacao, Carteira

admin.site.register(Transacao)
admin.site.register(Carteira)