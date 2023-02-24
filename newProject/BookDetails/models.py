from django.db import models

# Create your models here.

class Book(models.Model):
    BookId= models.IntegerField()
    Bookname= models.CharField(max_length=100)
    Author= models.CharField(max_length=3)
    Publication= models.CharField(max_length=15)
    CreateAt= models.DateField(auto_now_add=True)
    UpdateAt= models.DateField(auto_now=True)
    