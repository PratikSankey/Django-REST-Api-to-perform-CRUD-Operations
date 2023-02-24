from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    #Queryset is collection of data from database
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
