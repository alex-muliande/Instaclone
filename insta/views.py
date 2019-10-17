from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from users.forms import CommentForm


# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     context ={
#         'posts': posts
#     }
#     return render(request, 'index.html',context)  


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['caption', 'image_name' ,'image']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Post
    fields =['caption', 'image_name' ,'image']

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super ().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.profile:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.profile:
            return True
        return False




@login_required(login_url='/login/')
def likePost(request,image_id):
  image = Post.objects.get(pk = image_id)
  is_liked = False
  if image.likes.filter(id = request.user.id).exists():
      image.likes.remove(request.user)
      is_liked = False
  else:
      image.likes.add(request.user)
      is_liked = True
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def comment(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            post = Post.get_post(post_id)
            comment.post = post
            comment.save()
            return redirect('posts')
    else:
        comment_form = CommentForm()
    context = {
        "comment_form":comment_form,
    }
    return render(request, 'index.html', context)


@login_required
def commenting(request, post_id):
    posts = Post.objects.get(pk=post_id)
    context ={
        "posts":posts,
    }
    return render(request, 'comments.html', context)