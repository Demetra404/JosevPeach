from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/', BlogListView.as_view(), name='blog_main' ),
    path('blog/new/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit')
]