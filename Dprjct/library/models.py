from django.db import models


class Client(models.Model):
    id_client = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=20)
    client_lastname = models.CharField(max_length=20)
    client_mail = models.EmailField(max_length=200)
    CIN = models.CharField(unique=True, max_length=10)
    client_pwd = models.CharField(max_length=30)

    def __str__(self):
        return self.client_name + '  ' + self.client_lastname
class Books(models.Model):
    id_books = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    def __str__(self):
        return self.book_name

class Location(models.Model):
    client_id = models.OneToOneField(Client, on_delete=models.CASCADE, blank=True, null=True)
    books_id = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True)
    date_purchase = models.DateField()
    return_date = models.DateField()
    duration = models.IntegerField()

