import uuid
import base64
from django.conf import settings
from django.shortcuts import redirect, render

from aviculture.forms import CommandeForm
from .models import Commande, Poultry, Egg, Sales,Image
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CommandeForm
from django.urls import reverse

# Create your views here.

def index(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'aviculture/index.html', context)


def poultry_list(request):
    poultry = Poultry.objects.all()
    return render(request, 'aviculture/poultry_list.html', {'poultry': poultry})

def egg_list(request, poultry_id):
    poultry = Poultry.objects.get(id=poultry_id)
    eggs = Egg.objects.filter(poultry=poultry)
    return render(request, 'aviculture/egg_list.html', {'poultry': poultry, 'eggs': eggs})

def sales_list(request, poultry_id):
    poultry = Poultry.objects.get(id=poultry_id)
    sales = Sales.objects.filter(poultry=poultry)
    return render(request, 'aviculture/sales_list.html', {'poultry': poultry, 'sales': sales})

def commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            # Génération du numéro de commande unique
            nom = form.cleaned_data['nom']
            telephone = form.cleaned_data['telephone']
            numero_commande = f'{nom}-{telephone}'

            # Calculate the hash of the command number
            short_hash = generate_short_hash(numero_commande)    
            # Enregistrement de la commande dans la base de données
            commande = Commande(
                numero_commande=short_hash,
                nom=form.cleaned_data['nom'],
                telephone=form.cleaned_data['telephone'],
                option=form.cleaned_data['option'],
                commentaire=form.cleaned_data['commentaire']
            )
            commande.save()
            
            sujet = 'Nouvelle commande'
            message = f"Une nouvelle commande a été passée :\n nom: {form.cleaned_data['nom']}, \n email:  {form.cleaned_data['email']},\n telephone: {form.cleaned_data['telephone']},\n option: {form.cleaned_data['option']},\n commentaire: {form.cleaned_data['commentaire']}\n Numéro de commande : {numero_commande}"
            email_gerant = 'idiao310@gmail.com'  # Remplacez par l'adresse e-mail du gérant
            email_client = form.cleaned_data['email']  # Adresse e-mail du client
            send_mail(sujet, message, email_client, [email_gerant])
            messages.success(request, 'Votre commande a été envoyée avec succès.')
            
            command = Commande.objects.filter(nom=nom, telephone=telephone)
            context = {'commande': command}
            return render(request, 'aviculture/detail_commande.html', context)
    else:
        form = CommandeForm()
    
    context = {'form': form}
    return render(request, 'aviculture/commande.html', context)

def generate_command_number():
    # Logic to generate the command number
    # Replace this with your own implementation
    return "123456"

def generate_short_hash(data, length=10):
    # Generate a unique identifier using UUID
    unique_id = str(uuid.uuid4())

    # Encode the UUID using Base64
    encoded_id = base64.b64encode(unique_id.encode()).decode()

    # Take the first `length` characters of the encoded ID
    short_hash = encoded_id[:length]

    return short_hash

def detail_commande(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        
        try:
            commande = Commande.objects.filter(nom=nom, telephone=telephone)
            # Effectuez les opérations nécessaires avec la commande
            
            context = {'commande': commande}
            return render(request, 'aviculture/detail_commande.html', context)
        except Commande.DoesNotExist:
            messages.error(request, 'Aucune commande trouvée.')
    
    return render(request, 'aviculture/detail_commande.html')

