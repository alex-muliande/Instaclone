from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^like/(\d+)',views.likePost, name="likePost"),
    path('comment/<post_id>/', views.comment, name="comment"),
    path('commenting/<post_id>', views.commenting, name="commenting"),
]
