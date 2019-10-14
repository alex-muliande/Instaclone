from django.db import models
from django.contrib.auth.models import User

#   your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

    


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
