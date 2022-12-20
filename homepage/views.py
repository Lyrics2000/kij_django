from django.shortcuts import render
from .models import (BooksHolder,
PaperSizes,
Binding,
PaperFortext,
ColorFortext,
PrintedSideOfPapertext,
PaperCover,
ColorForCover,
PrintedSidesOfThePaperCover)

# Create your views here.



def index(request):

    all_books = BooksHolder.objects.all()
    all_paper_size = PaperSizes.objects.all()
    all_bindings = Binding.objects.all()
    all_paper_for_text = PaperFortext.objects.all()
    all_color_for_text = ColorFortext.objects.all()
    printed_sides = PrintedSideOfPapertext.objects.all()
    paper_cover = PaperCover.objects.all()
    color_for_cover =  ColorForCover.objects.all()
    printed_sides_of_paper = PrintedSidesOfThePaperCover.objects.all()

    context = {
        "all_books":all_books,
        "paper_size":all_paper_size,
        "all_bindings":all_bindings,
        "all_paper_for_text":all_paper_for_text,
        "all_color_for_text":all_color_for_text,
        "printed_sides":printed_sides,
        "paper_cover":paper_cover,
        "color_for_cover":color_for_cover,
        "printed_sides_of_paper":printed_sides_of_paper
    }
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')


def contact(request):

    return render(request,'contact.html')



def news(request):

    return render(request,'news.html')



def sifuBwana(request):

    return render(request,'sifuBwana.html')



def printing(request):

    return render(request,'printing.html')



def delivery(request):

    return render(request,'delivery.html')



def sifuniBwana2(request):
    return render(request,'product3.html')