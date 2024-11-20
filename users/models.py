from django.db import models
from django.contrib.auth.models import User
from PIL import Image

MAX_IMG_DIM = 256

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        img.thumbnail((256,256))
        img.save(self.image.path)
        
        
