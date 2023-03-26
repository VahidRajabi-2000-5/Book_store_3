from django.urls import path
from . import views

urlpatterns = [
    # path("", views.book_list_view, name='book_list'),
    path("", views.BookListView.as_view(), name='book_list'),
  
    # path('<int:pk>/', views.book_detail_view, name='book_detail'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
  
    # path("create/", views.book_create_view, name='book_create'),
    path("create/", views.BookCreateView.as_view(), name='book_create'),
  
    # path('<int:pk>/edit', views.book_update_view, name='book_update'),
    path('<int:pk>/edit', views.BookUpdateView.as_view(), name='book_update'),
  
    # path("<int:pk>/delete/", views.book_delete_view, name='book_delete'),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name='book_delete'),


]
