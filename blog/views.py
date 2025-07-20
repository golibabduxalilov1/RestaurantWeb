from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_list(req):
    posts = BlogPost.objects.filter(is_published=True)

    context = {
        "posts": posts,
    }

    return render(req, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    # Recent posts for sidebar
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:2]

    # Related posts (last 3 posts excluding current)
    related_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:2]

    context = {
        "post": post,
        "recent_posts": recent_posts,
        "related_posts": related_posts,
    }
    return render(request, "blog/blog_detail.html", context)

    return render(req, "blog/blog_detail.html", context)
