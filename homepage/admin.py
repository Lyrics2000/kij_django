from django.contrib import admin

# Register your models here.
from .models import (BooksHolder,
PaperSizes,
Binding,
PaperFortext,
ColorFortext,
PrintedSideOfPapertext,
PaperCover,
ColorForCover,
PrintedSidesOfThePaperCover)

admin.site.register(BooksHolder)
admin.site.register(PaperSizes)
admin.site.register(Binding) 
admin.site.register(PaperFortext)
admin.site.register(ColorFortext)
admin.site.register(PrintedSideOfPapertext)
admin.site.register(PaperCover)
admin.site.register(ColorForCover)
admin.site.register(PrintedSidesOfThePaperCover)
