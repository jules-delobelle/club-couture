from django.contrib import admin
from .models import Cotisant, Produit, Achat

# Register your models here.

@admin.register(Cotisant)
class CotisantAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "solde")
    search_fields = ("user__last_name", "user__first_name", "user__email")
    list_filter = ("solde",)
    ordering = ("user__last_name",)

    def nom(self, obj):
        return obj.user.last_name.upper()

    def prenom(self, obj):
        return obj.user.first_name.capitalize()

    def email(self, obj):
        return obj.user.email


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
    search_fields = ("cotisant__user__last_name", "produit__nom")
    date_hierarchy = "date"
    ordering = ("-date",)