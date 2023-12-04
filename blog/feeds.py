from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog newest posts"
    link = "/rss/feed"
    description = "My latest posts on blog"

    def items(self):
        return Post.objects.filter(status=True).order_by("-published_at")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:500]