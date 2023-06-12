from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('commande/', views.commande, name='commande'),
    path("detail_commande/",views.detail_commande,name="detail_commande")
]
