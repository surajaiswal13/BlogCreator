from django.urls import path
from blog.views import (
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    BlogListView,
    Search)

app_name = 'blog'

urlpatterns = [
    path('blogcreate/',BlogCreateView.as_view(),name='blogcreate'),
    path('<username>/<slug:blog_slug>/',BlogDetailView.as_view(),name='blogdetail'),
    path('<username>/<slug:blog_slug>/update/',BlogUpdateView.as_view(),name='blogupdate'),
    path('<username>/<slug:blog_slug>/delete/',BlogDeleteView.as_view(),name='blogdelete'),
    path('<username>/post-list',BlogListView.as_view(),name='bloglist'),
    path('search/',Search.as_view(),name='search')
]