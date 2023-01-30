from django.shortcuts import render ,redirect
from.models import Produit 
from django.core.paginator import Paginator

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm 




def index(request):
     
     datas={}
        
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
        'produit_object': produit_object
     }
     return render(request,"pages/shop.html",datas)

def news(request):
     
     datas={}
    
     return render(request,"pages/news.html",datas) 

def blog(request, myid):
    produit_object= Produit.objects.get(id=myid)
    datas = {
       'produit': produit_object
    }
    return render(request, 'pages/blog.html', datas)  


#def avis(request, pk, choice):
   # produit_object = Produit.objects.get(id=pk)
   # if choice == 'like':
    #    avi = Avis()
     #   avi.user = request.user
      #  avi.produit = produit_object
      #  avi.like = True 
      #  avi.save()
   # elif choice == 'dislike':
      #  avi = Avis()
      #  avi.user = request.user
       # avi.produit = produit_object
       # avi.like = False 
       # avi.save()
    #return redirect('blog', myid=produit_object.id)     






  

   





