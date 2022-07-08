#from django.shortcuts import render
from django.views.generic import ListView 
from .models import Editor

class BlogListView(ListView):
    model = Editor
    template_name = 'home.html'