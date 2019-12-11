from django.views.generic import TemplateView,ListView,DetailView,CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404,redirect,render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from blog.forms import PostForm
from django.utils import timezone

# Create your views here.

login_url_to_use = '/login/'
class AboutView(TemplateView) :
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte =timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView,LoginRequiredMixin):
    model = Post
    login_url = login_url_to_use
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

class PostUpdateView(UpdateView,LoginRequiredMixin):
    login_url = login_url_to_use
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy("post_list")
    form_class = PostForm

class DraftListView(LoginRequiredMixin,ListView):
    login_url = login_url_to_use
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).orderby("-created_date")


############################Commnt

@login_required(login_url=login_url_to_use)
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentFrom(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else :
        form = CommentForm()
        return  render(request,'blog.comment_form.html',{'form':form})

@login_required(login_url= login_url_to_use)
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required(login_url= login_url_to_use)
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk = post_pk)

@login_required(login_url=login_url_to_use)
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk = post_pk)







