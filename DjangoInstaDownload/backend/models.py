from django.db import models

# Create your models here.

class UploadImg(models.Model):
    post_image=models.ImageField(upload_to= 'uploads/')