from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfilePic(models.Model):
    image = models.ImageField(upload_to='profile/')
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='picture')