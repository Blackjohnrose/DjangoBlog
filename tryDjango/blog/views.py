from django.shortcuts import render

post = [
    {
        'auther': 'tryDjango',
        'title': 'Blog post 1',
        'content': 'the first content',
        'date_post': 'Feb 25, 2021 18:03:35'
    },
        {
        'auther': 'tryDjango 2',
        'title': 'Blog post 2',
        'content': 'the second content',
        'date_post': 'Feb 25, 2021 18:04:22'
    }
]


def home_view(request):
    context = {
        "post": post
    }

    return render(request, "blog/blog_home.html", post)


def about_view(request):

    return render(request, "blog/blog_about.html")
