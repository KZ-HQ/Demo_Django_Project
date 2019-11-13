from django.db import models
from django.contrib.auth.models import User
from main.models import Course
from PIL import Image

# Create your models here.


class Profile(models.Model):
    # One to One relationship with User model
    # If a User is deleted, the corresponding Profile will also be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Need to install Pillow python package for ImageField
    # A default.jpg file is used when user does not upload a profile image
    # else, if uploaded an image look in profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
