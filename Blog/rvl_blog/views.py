from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView)
from rvl_blog.models import Post, Comments


# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now().order_by('-publish_date'))

class PostListView(DetailView):

    model = Post