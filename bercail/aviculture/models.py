from django.db import models

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Poultry(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    productivity = models.FloatField()
    # Autres champs spécifiques à la volaille

    def __str__(self):
        return self.name

class Egg(models.Model):
    poultry = models.ForeignKey(Poultry, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} eggs from {self.poultry.name} on {self.date}"

class Sales(models.Model):
    poultry = models.ForeignKey(Poultry, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()
    # Autres champs spécifiques à la vente

    def __str__(self):
        return f"{self.quantity} sold from {self.poultry.name} on {self.date}"

class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prevention = models.TextField()

    def __str__(self):
        return self.name

class PoultryDisease(models.Model):
    poultry = models.ForeignKey(Poultry, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.poultry.name} - {self.disease.name}"


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Commande(models.Model):
    numero_commande = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    option = models.CharField(max_length=100)
    commentaire = models.TextField(blank=True)
    statut = models.CharField(max_length=100,default='En attente')
    date_commande = models.DateTimeField(auto_now_add=True)