# aviculture/forms.py

from django import forms

class CommandeForm(forms.Form):
    OPTIONS = [
        ('poussins', 'Poussins'),
        ('poulets', 'Poulets'),
        ('viande', 'Viande de poulet'),
    ]
    
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20)
    option = forms.ChoiceField(choices=OPTIONS)
    commentaire = forms.CharField(widget=forms.Textarea, required=False)
