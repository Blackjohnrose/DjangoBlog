from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):

    return render(request, "blog/blog_home.html")


def about_view(request):

    return render(request, "blog/blog_about.html")
