from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .manager import CustomUserManager
from .utils import generate_slug,send_email_to_register
# Create your models here.
class CustomUser(AbstractUser):
    username = None
    phone_no = models.CharField(max_length=20 )
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="profile")
    about_user = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Post(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self , *args,**kwargs):
        self.slug = generate_slug(self.title)
        super(Post,self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save,sender = CustomUser)
def call_account_email(sender, instance ,created, **kwargs):
     if created:
        recipient_email = instance.email    
        if recipient_email:
            send_email_to_register([recipient_email])
        else:
            print(f"Warning: User '{instance.username}' registered without an email address. No welcome email sent.")