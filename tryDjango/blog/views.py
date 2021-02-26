from django.shortcuts import render
from .models import Post

post = [
    {
        'author': 'tryDjango',
        'title': 'Blog post 1',
        'content': 'the first content',
        'date_posted': 'Feb 25, 2021 18:03:35'
    },
        {
        'author': 'tryDjango 2',
        'title': 'Blog post 2',
        'content': 'the second content',
        'date_posted': 'Feb 25, 2021 18:05:35'
    }
]


def home_view(request):
    post = Post.objects.all()
    context = {
        "post": post,
        "title": "Home"

    }

    return render(request, "blog/blog_home.html", context)


def about_view(request):

    return render(request, "blog/blog_about.html", {'title': 'About'})
