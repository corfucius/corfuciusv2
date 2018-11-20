from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Posts

def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def details(request, blog_id):
  post = get_object_or_404(Posts, pk=blog_id)
  context = {
      'post': post
  }
  return render(request, 'blog/details.html', context)
