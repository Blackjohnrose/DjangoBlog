from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
)
from .models import Post

def home_view(request):
    post = Post.objects.all()
    context = {
        "post": post,
        "title": "Home"

    }

    return render(request, "blog/blog_home.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about_view(request):

    return render(request, "blog/blog_about.html", {'title': 'About'})
