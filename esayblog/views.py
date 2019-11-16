from django.shortcuts import render

from esayblog.models import BlogPost


def index(request):

    posts = BlogPost.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)
