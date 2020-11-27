from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

def get_profile_image_filepath(self, filename):
    return f'profile_pics'

def get_default_profile_image():
    return "Groupwork-website.jpg"

class User(auth.models.User, auth.models.PermissionsMixin):
  
    def __str__(self):
        return "@{}".format(self.username)



class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=get_profile_image_filepath, default=get_default_profile_image)

    def get_profile_image_filename(self):
        return f'{self.user.username} Profile'

    

    
    
