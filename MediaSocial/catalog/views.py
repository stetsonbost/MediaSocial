from django.shortcuts import render

from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Author, Review, Genre, Music, Television, Reply
from django.contrib.auth.models import User
from .forms import ReplyForm

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    # Available books (status = 'a')
    num_authors=Author.objects.all().count()  # The 'all()' is implied by default.
    num_music=Music.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors,
            'num_visits':num_visits, 'num_music':num_music}, # num_visits appended
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
    #template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 3
    def get_queryset(self):
        return Music.objects.filter(song_title__icontains='')[:5] # Get 5 books containing the title war

class TelevisionListView(generic.ListView):
    model = Television
    context_object_name = 'television_list'   # your own name for the list as a template variable
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 3
    def get_queryset(self):
        return Television.objects.filter(title__icontains='')[:5] # Get 5 books containing the title war


class BookDetailView(generic.DetailView):
    model = Book

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'catalog/user_detail.html'

class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'catalog/review_detail.html'


class MusicDetailView(generic.DetailView):
    model = Music

class TelevisionDetailView(generic.DetailView):
    model = Television

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20

class AuthorDetailView(generic.DetailView):
    model = Author

class MediaView(generic.ListView):
    model = Author
    template_name = 'catalog/media.html'

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
