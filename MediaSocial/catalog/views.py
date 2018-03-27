from django.shortcuts import render

from django.views import generic

from .models import Book, Author, Comment, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    # Available books (status = 'a')
    num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 2
    def get_queryset(self):
        return Book.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    def get_queryset(self):
        return Author.objects.filter(first_name__icontains='')[:5]

class AuthorDetailView(generic.DetailView):
    model = Author
