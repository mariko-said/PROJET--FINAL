import graphene
from graphene_django import DjangoObjectType
from .models import Categorie, Contact, Vote,Produit,Commentaire

class CategorieType(DjangoObjectType):
    class Meta: 
        model = Categorie
        fields = ('nom' , )

  
class ContactType(DjangoObjectType):
    class Meta: 
        model = Contact
        fields = (
            'nom',
            'email',
            'numero',
            'sujet',
            'message', 
            
        )  

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
        fields = (
          'user',
            'produit',
            'valeur', 
        )

class ProduitType(DjangoObjectType):
    class Meta: 
        model = Produit
        fields = (
            'titre',
            'description',
            'image',
            'prix',
             
            
        )  

class CommentaireType(DjangoObjectType):
    class Meta: 
        model = Commentaire
        fields = (
            'nom',
            'email',
            'commentaire',
             
            
        )                        

class Query(graphene.ObjectType):
    categories = graphene.List(CategorieType)
    Contact = graphene.List(ContactType)
    Vote = graphene.List(VoteType)
    Commentaire = graphene.List(CommentaireType)
    Produit = graphene.List(ProduitType)

    def resolve_Categorie(root, info, **kwargs):
        # Querying a list
        return Categorie.objects.all()

    def resolve_Contact(root, info, **kwargs):
        # Querying a list
        return Contact.objects.all()

    def resolve_Vote(root, info, **kwargs):
        # Querying a list
        return Vote.objects.all()    

    def resolve_Produit(root, info, **kwargs):
        # Querying a list
        return Produit.objects.all() 

    def resolve_Commentaire(root, info, **kwargs):
        # Querying a list
        return Commentaire.objects.all()       


schema = graphene.Schema(query=Query)