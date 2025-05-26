from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user  = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
