from django.contrib import admin
from.models import Categorie,Produit,Contact ,Commentaire,Vote,CartProduit
#admin.site.site_header = "MARIKO"
#admin.site.site_title = 'MSK shop'

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add')
    search_fields = ['nom']


   
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'description', 'prix','date_add')
    search_fields = ['nom']
    #list_editable = ( 'prix')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add','email','numero')
    search_fields = ['nom']

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add','email','commentaire')
    search_fields = ['nom']
    


admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Vote)
admin.site.register(CartProduit)
admin.site.register(Commentaire,CommentaireAdmin)

