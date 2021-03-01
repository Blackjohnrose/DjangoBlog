from django.urls import path
from .views import (
    home_view,
    about_view,
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('about/', about_view, name="blog-about"),
    path('', PostListView.as_view() , name="blog-home"),
    path('post/new/', PostCreateView.as_view() , name="post-create"),
    path('post/<int:pk>/', PostDetailView.as_view() , name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name="post-delete"),
]
