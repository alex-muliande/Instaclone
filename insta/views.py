from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post


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
        if self.request.user == post.user:
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