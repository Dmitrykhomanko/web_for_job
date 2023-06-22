from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=50, default="хавчик")
    photo = models.ImageField(upload_to="for_gallery")

    def __str__(self):
        return self.name