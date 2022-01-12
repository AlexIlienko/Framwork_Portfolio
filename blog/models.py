from django.db import models


# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.name