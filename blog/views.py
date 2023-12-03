from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone
from django.core.paginator import (
   Paginator, EmptyPage,
   PageNotAnInteger
)

# Create your views here.
def blog_view(request, **kwargs):
    now = timezone.now()
    # url = request.POST.get('url')
    # print(url)
    posts = Post.objects.filter(status=True).exclude(published_at__gte=now)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()

    paginator = Paginator(posts, 6)
    try:
        page = request.GET.get('page')
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)

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