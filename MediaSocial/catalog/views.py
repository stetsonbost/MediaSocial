from django.shortcuts import render

from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Author, Review, Genre, Music

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    # Available books (status = 'a')
    num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors,
            'num_visits':num_visits}, # num_visits appended
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 3
    def get_queryset(self):
        return Book.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war

class MusicListView(generic.ListView):
    model = Music
    context_object_name = 'music_list'   # your own name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 3
    def get_queryset(self):
        return Music.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20
    def get_queryset(self):
        return Author.objects.filter(first_name__icontains='')[:5]

class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_birth':'05/01/2018',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title','author','isbn','genre', 'summary']
