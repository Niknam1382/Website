from django.db import models
from django.contrib.auth.models import User

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
    # tag
    counted_view = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(auto_now=True, null=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.title