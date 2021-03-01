from django.urls import path
from .views import home_view, about_view, PostListView

urlpatterns = [
    path('', PostListView.as_view() , name="blog-home"),
    path('about/', about_view, name="blog-about"),

]
