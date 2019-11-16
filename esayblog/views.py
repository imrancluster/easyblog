from django.shortcuts import render, get_object_or_404

from esayblog.models import BlogPost


def index(request):

    posts = BlogPost.objects.all()

    context = {
        'posts': posts.order_by('-created_at')
    }

    return render(request, 'index.html', context)

def view_post(request, post_id):

    post = get_object_or_404(BlogPost, pk=post_id)

    return render(request, 'post.html', {'post': post})

