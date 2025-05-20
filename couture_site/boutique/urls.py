from django.urls import path
from .views import acheter_produit

urlpatterns = [
    path('acheter/', acheter_produit, name='acheter'),
]
