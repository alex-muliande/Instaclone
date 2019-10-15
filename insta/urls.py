from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='insta-home '),
    path('post/<int:pk>/', PostListView.as_view(), name='post-detail'),
]
