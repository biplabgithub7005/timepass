from django.db import models

# Create your models here.
from datetime import datetime
from accounts.models import Signup
STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)
class Posts(models.Model):
    image =models.ImageField(default='post.png', upload_to='posts')
    file =models.FileField(default="video", upload_to='files')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)
    user =models.ForeignKey(Signup, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='published')

    def __str__(self):
        return self.title
