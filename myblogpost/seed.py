from faker import Faker
from django.contrib.auth import get_user_model
from .models import Post
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
import random
import requests
fake = Faker()

def seed_db(n=10):
   
    User = get_user_model()
    
    # Create or get a default user
    try:
        default_user = User.objects.get(email="seed_user@example.com")
    except User.DoesNotExist:
        default_user = User.objects.create_user(
            email="seed_user@example.com",
            password='seed123#',
            first_name='Seed',
            last_name='User',
            phone_no=fake.phone_number(),
            about_user="A user created by the seeder."
        )
    for _ in range(n):
        title = fake.catch_phrase()
        content = fake.text(max_nb_chars=2000)

        # Get a placeholder image from the internet
        img_url = "https://picsum.photos/600/400"
        response = requests.get(img_url)
        file = ContentFile(response.content)
        filename = fake.file_name(extension="png")

        # Pick a random user

        Post.objects.create(
            user = default_user,
            title=title,
            content=content,
            img=SimpleUploadedFile(name=filename, content=file.read(), content_type='image/png'),
        )

    print(f"✅ Successfully created {n} fake posts.")
