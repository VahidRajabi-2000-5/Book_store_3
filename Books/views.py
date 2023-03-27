from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from .models import Book
from .forms import BookForm


# def book_list_view(request):
#     book = Book.objects.all().order_by("-id")
#     return render(request, 'book/book_list.html', {'book': book})
# ==========================================================================
# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'book/book_detail.html', {'book': book})
# ======================================================================================

# def book_create_view(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'book/book_create.html', {'form': form})
# ----------------------
# class BookCreateView(generic.CreateView):
#     form_class = BookForm
#     template_name = 'book/book_create.html'
#     context_object_name = 'form'
# ===================================================
# def book_update_view(request, pk):
#     # book به خاطر اینکه بزاریم در تایتل سایت عنوان نمایش داده بشه
#     book = get_object_or_404(Book, pk=pk)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('book_detail', args=[book.id]))
#     return render(request, 'book/book_update.html', {'form': form, 'book': book})
# --------------------------------------------------------------
# class BookUpdateView(generic.UpdateView):
#     model = Book
#     form_class = BookForm
#     template_name = 'book/book_update.html'
#     context_object_name = 'form'
#     context_object_name = 'book'

# ======================================================================
# def book_delete_view(request,pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method =='POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request,'book/book_delete.html',{'book':book})


class BookListView(generic.ListView):
    # model = Book
    paginate_by = 1
    template_name = 'book/book_list.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.all().order_by("-id")


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = [
        'عنوان',
        'نویسنده',
        'توضیحات',
        'مترجم',
        'ناشر',
        'تعداد_صفحات',
        'قیمت',
        'cover',
    ]
    template_name = 'book/book_create.html'
    context_object_name = 'form'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = [
        'عنوان',
        'نویسنده',
        'توضیحات',
        'مترجم',
        'ناشر',
        'تعداد_صفحات',
        'cover',
    ]

    template_name = 'book/book_update.html'
    context_object_name = 'form'
    context_object_name = 'book'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')
