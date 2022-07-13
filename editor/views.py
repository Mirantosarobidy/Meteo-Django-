#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ( CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Editor

class BlogListView(ListView):
    model = Editor
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Editor
    template_name= 'editor_detail.html'
    
class BlogCreateView(CreateView):
    model = Editor
    template_name= 'editor_new.html'
    fields = ['title',  'author', 'body']
    
class BlogUpdateView(UpdateView):
    model = Editor
    template_name = 'editor_edit.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Editor
    template_name = 'editor_delete.html'
    success_url = reverse_lazy('home')