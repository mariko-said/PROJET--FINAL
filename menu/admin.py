from django.contrib import admin
from.models import Categorie,Produit,Contact



class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add')
    search_fields = ['nom']
    
   
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre',"image", 'categorie', 'description', 'prix','date_add')
    search_fields = ['nom']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add','email','numero')
    search_fields = ['nom']

#class CommentaireAdmin(admin.ModelAdmin):
    #list_display = ('nom', 'date_add','email','commentaire')
    #search_fields = ['nom']    

admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Contact,ContactAdmin)
#admin.site.register(Avis)
#admin.site.register(Tag)
#admin.site.register(Commentaire,CommentaireAdmin)

