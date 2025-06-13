from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
from uuid import uuid4

def send_email_to_register(recipients):
    subject = "Congratulations! You are registered in Blogify"
    message = '''Hi,
    You are now registered in Blogify.
    You can now write any blogs you want.
    Please join this Telegram link to connect one-on-one: https://t.me/+ui06untQfbo3MzU
    If you have any issues, don't hesitate; we are here.
    Write to us on: blogify@gmail.com
    Keep Writing,
    Blogify'''
    from_email = settings.EMAIL_HOST_USER
    
    if not isinstance(recipients, list):
        recipients = [recipients]

    print(f"DEBUG: Attempting to send registration email to: {recipients}") 
    try:
        send_mail(subject, message, from_email, recipients, fail_silently=False)
        print("DEBUG: Email sent successfully!")
    except Exception as e:
        print(f"ERROR: Failed to send email: {e}")

def generate_slug(title:str)->str:
    from .models import Post
    base_slug = slugify(title)  # Converts to URL-friendly format
    slug = base_slug
    counter = 1

    while Post.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{str(uuid4())[:4]}"  # add 4-char unique suffix
        counter += 1

    return slug