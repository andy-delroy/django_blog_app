from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):
    posts = BlogPost.objects.order_by('date_created') 
    post_dict = {}
    #associate each post whith its image url
    for post in posts:
        post_dict[post] = post.images.first().image

    return render(request, 'blog/index.html', {
        'posts': posts,
        'post_dict': post_dict,
    })

def post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    #is not necessary to get all but might improve later
    images = post.images.all()
    image_dict = {}
    for image in images:
        image_dict[image.image_order] = image.image
        print(image.image)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'images': images,
        'image_dict': image_dict,
    })