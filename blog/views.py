from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone

# Create your views here.
def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status=True).exclude(published_at__gte=now)
    if kwargs.get('cat_name') is not None:
        posts = Post.objects.filter(status=True, category__name=kwargs['cat_name']).exclude(published_at__gte=now)
    
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    context = {'posts': posts, 'categories':cat_dict}
    return render(request, 'blog.html', context)

def blog_single(request, pid):
    now = timezone.now()
    posts = Post.objects.filter(status=True).exclude(published_at__gte=now)
    post = get_object_or_404(posts, pk=pid)
    prev = Post.objects.filter(status=1, created_at__lt=post.created_at).exclude(pk=post.pk).order_by('-created_at').first()
    next = Post.objects.filter(status=1, created_at__gt=post.created_at).exclude(pk=post.pk).order_by('created_at').first()
    post.counted_view += 1
    post.save()
    context = {'post': post, 'next': next, 'prev': prev}
    return render(request, 'single-post.html', context)