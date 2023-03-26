from django.db import models
from django.urls import reverse

class Book(models.Model):
    عنوان = models.CharField(max_length=200)
    نویسنده = models.CharField(max_length=200)
    توضیحات = models.TextField()
    مترجم =models.CharField(max_length=150)
    ناشر =models.CharField(max_length=150)
    تعداد_صفحات = models.PositiveIntegerField()
    قیمت = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    def __str__(self):
        return self.عنوان
    
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    