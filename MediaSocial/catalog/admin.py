from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, Review, Reply, Music, Television

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Reply)
admin.site.register(Music)
admin.site.register(Television)
