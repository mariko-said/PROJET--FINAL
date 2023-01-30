
from django.urls import path
from.import views
app_name = 'menu'
urlpatterns = [
    path("",views.index,name="index"),
    #path("/<int:myid>",views.blog,name="blog"),
    path("news",views.news,name="news"),
    path("blog",views.blog,name="blog"),
    path("buy",views.buy,name="buy"),
    path("shop",views.shop,name="shop"),
    path("contact/", views.contact, name="contact"),
    
  
   
    
]