from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    date_add=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-date_add"]

    def __str__(self) -> str:
        return self.nom    

class Produit(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=5000) # permet d'indiquer le fichier où recuperer les images
    prix = models.FloatField()
    categorie = models.ForeignKey(Categorie,related_name="Categorie", on_delete=models.CASCADE)
    date_add=models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-date_add","-date_update"]

    def __str__(self) -> str:
        return self.titre

class Contact(models.Model):
    nom =  models.CharField(max_length=100)
    numero = models.FloatField()
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_add=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-date_add"]

    def __str__(self):
        return self.email  

class Commentaire(models.Model):
    nom = models.CharField(max_length=150)
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE, related_name='commentaire')
    email = models.EmailField()
    commentaire = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
       ordering=["-date_add","-date_update"]

    def __str__(self) :
       return self.nom

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    valeur = models.BooleanField(default=True) # True for Like, False for Dislike

class CartProduit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

