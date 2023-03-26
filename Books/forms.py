from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "عنوان",
            "نویسنده",
            "توضیحات",
            "مترجم",
            "ناشر",
            "تعداد_صفحات",
            "قیمت",
        ]