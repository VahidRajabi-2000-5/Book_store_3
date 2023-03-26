from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCrationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCrationForm
    template_name = 'registration/signup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')
