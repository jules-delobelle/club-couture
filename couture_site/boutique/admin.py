from django.contrib import admin
from .models import Cotisant, Produit, Achat

# Register your models here.

@admin.register(Cotisant)
class CotisantAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "solde")
    search_fields = ("nom", "prenom", "email")
    list_filter = ("solde",)
    ordering = ("nom",)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix", "stock")
    list_editable = ("prix", "stock")
    search_fields = ("nom",)
    ordering = ("nom",)

@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ("produit", "cotisant", "date", "quantite")
    list_filter = ("date","produit")
    search_fields = ("cotisant__nom", "produit__nom")
    date_hierarchy = "date"
    ordering = ("-date",)