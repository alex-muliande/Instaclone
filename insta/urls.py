from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^like/(\d+)',views.likePost, name="likePost"),
]
