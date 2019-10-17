from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#   your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='users/', default='user.png')
    bio = models.TextField(default="Welcome!")

    def __str__(self):
        return f'{self.user.username} Profile' 
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class Post(models.Model):
    image_name = models.CharField(max_length = 30)
    caption = models.TextField(default="Welcome Me!")
    image = models.ImageField(upload_to='posts/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)
    
    def total_likes(self):
        self.likes.count()

    def __str__(self):
        return self.image_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment