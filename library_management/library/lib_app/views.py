from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from django.core.exceptions import MultipleObjectsReturned

def book_list(request):
    books = Book.objects.all()
    return render(request, 'lib_app/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'lib_app/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        author_id = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        available_copies = request.POST.get('available_copies')

        # Check if a new author name is provided
        if author_name:
            try:
                author, created = Author.objects.get_or_create(name=author_name)
            except MultipleObjectsReturned:
                author = Author.objects.filter(name=author_name).first()
        else:
            author = get_object_or_404(Author, id=author_id)

        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date, available_copies=available_copies)

        return redirect('book_list')
    
    authors = Author.objects.all()
    unique_authors = {author.name: author for author in authors}.values()
    return render(request, 'lib_app/book_create.html', {'authors': unique_authors})

def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.isbn = request.POST.get('isbn')
        author_name = request.POST.get('author_name')
        author_id = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.available_copies = request.POST.get('available_copies')

        # Check if a new author name is provided
        if author_name:
            try:
                author, created = Author.objects.get_or_create(name=author_name)
            except MultipleObjectsReturned:
                author = Author.objects.filter(name=author_name).first()
        else:
            author = get_object_or_404(Author, id=author_id)

        book.author = author
        book.save()

        return redirect('book_list')
    
    authors = Author.objects.all()
    unique_authors = {author.name: author for author in authors}.values()
    return render(request, 'lib_app/book_update.html', {'book': book, 'authors': unique_authors})

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'lib_app/book_delete.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    unique_authors = {author.name: author for author in authors}.values()
    return render(request, 'lib_app/author_list.html', {'authors': unique_authors})

def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        biography = request.POST.get('biography')
        try:
            author, created = Author.objects.get_or_create(name=name, defaults={'biography': biography})
            if not created:
                author.biography = biography
                author.save()
        except MultipleObjectsReturned:
            author = Author.objects.filter(name=name).first()
            author.biography = biography
            author.save()
        return redirect('author_list')
    
    return render(request, 'lib_app/author_create.html')

def author_update(request, id):
    author = get_object_or_404(Author, id=id)

    if request.method == 'POST':
        author.name = request.POST.get('name')
        author.biography = request.POST.get('biography')
        author.save()
        return redirect('author_list')
    
    return render(request, 'lib_app/author_update.html', {'author': author})
