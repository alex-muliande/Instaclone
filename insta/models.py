from django.db import models
from django.contrib.auth.models import User

#   your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  
    profile_picture = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

    def __str__(self):
        return f'{self.user.username} Profile' 

    


class Post(models.Model):
    image_name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='posts/')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
