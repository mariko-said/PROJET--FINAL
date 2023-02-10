from django.shortcuts import render ,redirect
from.models import Produit,Vote,Commentaire,CartProduit
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import ContactForm, CommentaireForm

from django.views.decorators.csrf import csrf_protect


def index(request):
     produit_object= Produit.objects.all()
     datas={
        'produit_object': produit_object
         }
        
     return render(request,"pages/index.html",datas)
 

def buy(request):
    datas={}
    return render(request,"pages/buy.html",datas)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/contact.html', context)
    

def shop(request):
     produit_object= Produit.objects.all()
     paginator = Paginator(produit_object,4 )
     page = request.GET.get('page')
     produit_object = paginator.get_page(page)
     datas={
        'produit_object': produit_object ,
     }
     return render(request,"pages/shop.html",datas)

def news(request):
     
     datas={}
    
     return render(request,"pages/news.html",datas) 

def blog(request,myid):
     produit_object= Produit.objects.get(id=myid)
     likes = Vote.objects.filter(produit=produit_object, valeur=True).count()
     dislikes = Vote.objects.filter(produit=produit_object, valeur=False).count()
     comments = Commentaire.objects.all()
     datas = {
        "produit": produit_object,
        'comments': comments,
        'likes': likes,
        'dislikes': dislikes
        }
     return render(request, 'pages/blog.html', datas) 


def like(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    Vote.objects.create(user=request.user, produit=produit, valeur=True)
    return redirect('menu:blog', myid=myid)

   

def dislike(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    Vote.objects.create(user=request.user, produit=produit, valeur=False)
    return redirect('menu:blog', myid=myid)
     


def add_comment(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render( request,'pages/success.html')
    else:
        form = CommentaireForm()
    return render(request, 'pages/add_comment.html', {'form': form})  


def panier(request):
    cart_articles = CartProduit.objects.filter(user=request.user)
    return render(request, 'panier.html', {'cart_articles': cart_articles})

def remove_from_cart(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    cart_produit = CartProduit.objects.get(produit=produit, user=request.user)
    cart_produit.delete()
    return redirect('panier')
  

@csrf_protect
def add_panier(request, article_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            article = get_object_or_404(Produit, id=article_id)
            cart_article, created = CartProduit.objects.get_or_create(
                article= article,
                user=request.user
            )
            if not created:
                cart_article.quantity += 1
            cart_article.save()
            return redirect('panier')
        else:
            return redirect('connexion')
    

   
#def like_produit(request, myid):
  #  produit = get_object_or_404(Produit, id=myid)
  #  like_dislike, created = LikeDislike.objects.get_or_create(
       # produit=produit,
      #  user=request.user,
      #  defaults={'value': True}
  #  )
   # if not created:
    #    like_dislike.value = True
    #    like_dislike.save()
  #  return redirect('blog', myid=produit.id)

#def dislike_produit(request, myid):
   # produit = get_object_or_404(Produit, id=myid)
   # like_dislike, created = LikeDislike.objects.get_or_create(
    #    produit=produit,
    #    user=request.user,
     #   defaults={'value': False}
   # )
   # if not created:
    #    like_dislike.value = False
  #      like_dislike.save()
  #  return redirect('blog', myid=produit.id)




  

   





