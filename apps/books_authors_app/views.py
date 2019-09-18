from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.


# index of all books
def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books_authors_app/index.html', context)


# show book with id
def show(request, number):
    book = Book.objects.get(id=number)
    books_authors = book.authors.all()
    excluded_list = Author.objects.all()
    for author in books_authors:
        excluded_list = excluded_list.exclude(id=author.id)
    print(excluded_list)
    context = {
        'book': Book.objects.get(id=number),
        'filtered_authors': excluded_list
    }
    return render(request, 'books_authors_app/show.html', context)


# create new book
def new_book(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Book.objects.create(title=title, desc=description)
    return redirect('/')


# link existing author to existing book
def add_author_to_book(request):
    if request.method == "POST":
        author_id = request.POST['author_id']
        book_id = request.POST['book_id']
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=book_id)
        book.authors.add(author)
    return redirect('/books/'+str(book_id))


# show all authors
def index_author(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'books_authors_app/index_author.html', context)


# show specific author with id
def show_author(request, number):
    author_books = Author.objects.get(id=number).books.all()
    excluded_list = Book.objects.all()
    for book in author_books:
        excluded_list = excluded_list.exclude(id=book.id)
    context = {
        'author': Author.objects.get(id=number),
        'filtered_book': excluded_list
    }
    return render(request, 'books_authors_app/show_author.html', context)


# create new author
def new_author(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name=first_name,
                              last_name=last_name, notes=notes)
    return redirect('/authors')


# link existing book to existing author
def add_book_to_author(request):
    if request.method == "POST":
        book_id = request.POST['book_id']
        author_id = request.POST['author_id']
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=author_id)
        author.books.add(book)
    return redirect('/authors/'+str(author_id))
