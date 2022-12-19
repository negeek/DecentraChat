from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

# Create your models here.
from django.core.files.storage import default_storage
from io import BytesIO
from pathlib import Path

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE)

    profile_name = models.CharField(
        max_length=100, blank=True)

    avatar = models.FileField(
        default='default.jpg', upload_to='profile_images/')
    # resizing images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_types = {
            "jpg": "JPEG",
            "jpeg": "JPEG",
            "png": "PNG",
            "gif": "GIF",
            "tif": "TIFF",
            "tiff": "TIFF",
        }
        memfile = BytesIO()
        img = Image.open(self.avatar)
        if img.height >  128 or img.width > 128:
            output_size = (128, 128)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img_filename = Path(self.avatar.file.name).name
            img_suffix = Path(self.avatar.file.name).name.split(".")[-1]
            img_format = image_types[img_suffix]
            img.save(memfile, img_format, quality=95)
            default_storage.save(self.avatar.name, memfile)
            memfile.close()
            img.close()


    def __str__(self):
        return self.user.username
