from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('media/', views.MediaView.as_view(), name='media'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    path('review/create', views.ReviewCreate.as_view(), name='review_create'),
    path('reply/create', views.ReplyCreate.as_view(), name='reply_create'),
    path ('books/', views.BookListView.as_view(), name='books'),
    path ('music/', views.MusicListView.as_view(), name='music'),
    path ('music/<int:pk>', views.MusicDetailView.as_view(), name='music-detail'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),

]
