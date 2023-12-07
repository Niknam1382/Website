from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('last-post.html')
def lastpost(arg=6):
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-created_at')[:arg]
    return {'posts':posts}