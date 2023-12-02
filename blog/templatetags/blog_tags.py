from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name = 'Total_posts')
def function():
    Counter = Post.objects.filter(status = True).count()
    return Counter