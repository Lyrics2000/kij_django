from django.shortcuts import render
from .models import (BooksHolder,
PaperSizes,
Binding,
PaperFortext,
ColorFortext,
PrintedSideOfPapertext,
PaperCover,
ColorForCover,
PrintedSidesOfThePaperCover,
Banner,
AboutTeam,
KijabeSerivices)

# Create your views here.



def index(request):

    kijabe_services =  KijabeSerivices.objects.all()
    all_books = BooksHolder.objects.all()
    all_paper_size = PaperSizes.objects.all()
    all_bindings = Binding.objects.all()
    all_paper_for_text = PaperFortext.objects.all()
    all_color_for_text = ColorFortext.objects.all()
    printed_sides = PrintedSideOfPapertext.objects.all()
    paper_cover = PaperCover.objects.all()
    color_for_cover =  ColorForCover.objects.all()
    printed_sides_of_paper = PrintedSidesOfThePaperCover.objects.all()
    bb =  Banner.objects.all()

    context = {
        "all_books":all_books,
        "home_nav":"active",
        "nav_about":"",
        "nav_sifu_bwana":"",
        "nav_news":"",
        "nav_get_a_quote":"",
        "nav_contact":"",
        "kijabe_services":kijabe_services,


        "paper_size":all_paper_size,
        "all_bindings":all_bindings,
        "all_paper_for_text":all_paper_for_text,
        "all_color_for_text":all_color_for_text,
        "printed_sides":printed_sides,
        "paper_cover":paper_cover,
        "color_for_cover":color_for_cover,
        "printed_sides_of_paper":printed_sides_of_paper,
        "banner":bb
    }
    return render(request,'index.html',context)


def about(request):

    team =  AboutTeam.objects.all()


    context = {
         "home_nav":"",
        "nav_about":"active",
        "nav_sifu_bwana":"",
        "nav_news":"",
        "nav_get_a_quote":"",
        "nav_contact":"",
        "team":team
    }
    return render(request,'about.html',context)


def contact(request):
    context = {
         "home_nav":"",
        "nav_about":"",
        "nav_sifu_bwana":"",
        "nav_news":"",
        "nav_get_a_quote":"",
        "nav_contact":"active",
    }
    return render(request,'contact.html',context)



def news(request):
    context = {
         "home_nav":"",
        "nav_about":"",
        "nav_sifu_bwana":"",
        "nav_news":"active",
        "nav_get_a_quote":"",
        "nav_contact":"",
    }
    return render(request,'news.html',context)



def sifuBwana(request):
    context = {
     "home_nav":"",
        "nav_about":"",
        "nav_sifu_bwana":"active",
        "nav_news":"",
        "nav_get_a_quote":"",
        "nav_contact":"",
   }
    return render(request,'sifuBwana.html',context)



def printing(request):

    return render(request,'printing.html')



def delivery(request):

    return render(request,'delivery.html')



def sifuniBwana2(request):
    return render(request,'product3.html')