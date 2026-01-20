from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Blog
# Create your views here.

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_blog += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_main.html'
    context_object_name = 'blog_main'

    def get_queryset(self):
        return Blog.objects.filter(is_publication = True)

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title_blog', 'content_blog','views_blog']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_main')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title_blog', 'content_blog']
    template_name = 'blog/blog_form.html'
    #success_url = reverse_lazy('blog_main')

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_main')
