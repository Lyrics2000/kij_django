from django.urls import path
from .views import (index,about,contact,
news,
sifuBwana,
printing,
delivery,
sifuniBwana2)

app_name = "homepage"

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("news/",news,name="news"),
    path("sifuBwana/",sifuBwana,name="sifuBwana"),
    path("printing/",printing,name="printing"),
    path("delivery/",delivery,name="delivery"),
    path("sifuniBwana2/",sifuniBwana2,name="sifuniBwana2")
  
]