from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, Review, Reply

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Reply)
