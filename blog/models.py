from django.db import models
from django.contrib.auth.models import User
# from jalali_date import datetime2jalali, date2jalali
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_view = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(auto_now=True, null=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.title
    
    # def test (self):
    #     return date2jalali(self.published_at)
    
    def get_absolute_url(self) :
        return reverse('blog:single', kwargs={'pid':self.id})
    
class link(models.Model):
    url = models.CharField(max_length=255)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    # subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name+' '+self.last_name