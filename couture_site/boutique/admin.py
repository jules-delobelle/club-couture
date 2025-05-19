from django.contrib import admin
from .models import Cotisant, Produit, Achat

# Register your models here.

admin.site.register(Cotisant)
admin.site.register(Produit)
admin.site.register(Achat)