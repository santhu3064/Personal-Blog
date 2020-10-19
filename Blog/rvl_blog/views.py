from django.shortcuts import render
from rvl_blog.forms import PostForm, CommentsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from rvl_blog.models import Post, Comments
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

class AboutView(TemplateView):
    template_name = 'rvl_blog/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'rvl_blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'rvl_blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'rvl_blog/post_detail.html'
    success_url = reverse_lazy('post_list')

    model = Post


class PostDraftView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-date_created')


#######################################################
###############COMMENTS SECTION########################
#######################################################

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)




def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'rvl_blog/comments_form.html', {'form': form})

@login_required
def comments_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return  redirect('post_detail', pk=comment.post.pk)

@login_required
def comments_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return  redirect('post_detail', pk=post_pk)