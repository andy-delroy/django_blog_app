from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(max_length=200, unique = True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image_order = models.IntegerField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')
    # The image column is an ImageField field that works with the Django's file storage API

    def __str__(self):
        return self.title