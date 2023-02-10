
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views
app_name = 'menu'
urlpatterns = [
    path("",views.index,name="index"),
    path("<int:myid>",views.blog , name="blog"),
    path('<int:myid>/like/', views.like, name='like'),
    path('<int:myid>/dislike/', views.dislike, name='dislike'),
    path('add_comment', views.add_comment, name='add_comment'),
    path("news",views.news,name="news"),
    path("blog",views.blog,name="blog"),
    path("buy",views.buy,name="buy"),
    path("shop",views.shop,name="shop"),
    path("contact/", views.contact, name="contact"),
    path('panier/', views.panier, name='panier'),
    path('add_panier/<int:produit_id>/', views.add_panier, name='add_panier'),
    path('remove_from_cart/<int:produit_id>/', views.remove_from_cart, name='remove_from_cart'),
   
  
  
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)