from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path('', home_view, name="blog-home"),
    path('about/', about_view, name="blog-about"),

]
