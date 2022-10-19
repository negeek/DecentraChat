from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE)

    profile_name = models.CharField(
        max_length=100, blank=True)

    avatar = models.FileField(
        default='default.jpg', upload_to='profile_images/')

    def __str__(self):
        return self.user.username
