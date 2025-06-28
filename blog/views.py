from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic import (CreateView, 
                                  UpdateView 
                          )                              
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post-list.html'

# details view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    
    

class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']
    
   
   
# UpdateView 
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']
    
    
