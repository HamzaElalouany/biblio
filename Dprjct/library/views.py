from django.http import HttpResponse
from .models import Books

def index(request):
    all_books = Books.objects.all()
    html = ''
    for book in all_books:
        url = '/library/' + str (book.id_books) + '/'
        html += '<a href= "' + url + '">'+ book.book_name + '</a><br>'
    return HttpResponse(html)
def detail(request, books_id):
    return HttpResponse("here is the book number : "+str(books_id))
