from django.db import models
import os
import random

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "image/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )



class BooksHolder(models.Model):
    book_title = models.CharField(max_length=255)
    book_link = models.URLField()
    book_image = models.FileField(upload_to=upload_image_path)

    def __str__(self) -> str:
        return self.book_title




class PaperSizes(models.Model):
    paper_size = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.paper_size


class Binding(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class PaperFortext(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name


class ColorFortext(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class PrintedSideOfPapertext(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class PaperCover(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name


class ColorForCover(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name


class PrintedSidesOfThePaperCover(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Banner(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.TextField()
    image = models.FileField(upload_to=upload_image_path)


    def __str__(self) -> str:
        return self.subtitle



class AboutTeam(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    


    def __str__(self) -> str:
        return self.name



class KijabeSerivices(models.Model):
    service_image =  models.FileField(upload_to=upload_image_path)
    service_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.service_name


class PlaystoreBook(models.Model):
    name  = models.CharField(max_length=255)
    price = models.CharField(max_length=255, blank=True,null=True)
    book_description = models.CharField(max_length=255,blank=True,null=True)
    sifuBwana = models.BooleanField(default=False)
    book_image = models.FileField(upload_to=upload_image_path,blank=True,null=True)

    url = models.URLField()


    def __str__(self) -> str:
        return self.name


