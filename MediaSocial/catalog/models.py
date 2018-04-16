from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from datetime import date
from django.contrib.auth.models import User



class Review(models.Model):
    """ Model representing a comment"""

    description = models.CharField(max_length=500, help_text="Enter a comment...")

    mediaItem = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

class Reply(models.Model):
    """ Model representing a comment"""

    description = models.CharField(max_length=500, help_text="Enter a comment...")

    reply_to = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('book-detail', args=[str(self.id)])


class Music (models.Model):
    song_title = models.CharField(max_length=200)
    artist = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    length = models.FloatField(default=2.0)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.song_title

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('music-detail', args=[str(self.id)])


class Visual (models.Model):
    creator = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)


class Television(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    seasons = models.IntegerField(default = 1)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField('Genre')
    first_air_date = models.DateField(default=date.today())

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('television-detail', args=[str(self.id)])

class Movies(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Author', on_delete = models.CASCADE, related_name="director")
    writer = models.ForeignKey('Author', on_delete = models.CASCADE, related_name="writer")
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField('Genre')
    duration = models.IntegerField(default=30)
    release_date = models.DateField(default=date.today())

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
