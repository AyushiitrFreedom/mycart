from django.db import models

# Create your models here.
class Book(models.Model):
    Book_id = models.AutoField
    Book_name = models.CharField(max_length=50)
    book_price = models.IntegerField()
    