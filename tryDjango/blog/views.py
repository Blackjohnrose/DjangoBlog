from django.shortcuts import render
from .models import Post

def home_view(request):
    post = Post.objects.all()
    context = {
        "post": post,
        "title": "Home"

    }

    return render(request, "blog/blog_home.html", context)


def about_view(request):

    return render(request, "blog/blog_about.html", {'title': 'About'})
