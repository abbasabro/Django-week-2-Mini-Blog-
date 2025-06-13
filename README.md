# 📝 Django BlogPost Website

This is a **basic blog application** built with Django as part of my learning journey. It includes **user authentication**, **form handling**, and full **CRUD operations** for blog posts. The goal was to practice deeper Django concepts like advanced models, manual and model forms, messages framework, and session-based authentication.

---

## 🚀 Features

✅ User Registration & Login (manual Django forms)  
✅ Session-based Authentication (users stay logged in even after server restarts)  
✅ Add Blog Posts (ModelForm)  
✅ View All Blogs on Home Page  
✅ Search Blogs by Title or Content  
✅ Read More – Detailed View of Each Blog  
✅ My Blogs Section with Update/Delete Functionality  
✅ Django Messages Framework for User Feedback  
✅ Clean and Responsive UI using Bootstrap  

---

## 🛠️ Technologies Used

- Python 3.12.3 
- Django 5.2.1 
- SQLite (default Django database)  
- Bootstrap 5  
- HTML5, CSS3  
- Django Messages Framework  
- Django Forms & ModelForms  

---

## 📂 Project Structure

```
blogpost/
├── myblogpost/         # Main App
│   ├── models.py       # Blog Post model
│   ├── forms.py        # Manual and Model Forms
│   ├── views.py        # Views for auth & CRUD
│   ├── seed.py         # Add fake data
│   ├── manager.py      # Custom User model manager
│   ├── utils.py        # Extra Email and Slug related code
│   ├── templates/      # All HTML templates
│   └── static/         # Static files (CSS, JS)
├── blogpost/           # Project config folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3          # Database file
├── manage.py
└── README.md
```

---

## 🔐 Authentication Info

- User registration and login are built using manual `forms.Form`  
- Blog post creation uses `forms.ModelForm`  
- Authenticated views use Django’s session middleware  
- Users can only update or delete **their own** blogs  

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/abbasabro/django-blogpost.git

# Navigate into the project
cd django-blogpost

# Create virtual environment
python -m venv venv
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

Then visit http://127.0.0.1:8000/ in your browser.

---

## 📚 What I Learned

This project was a significant step in my Django learning journey. Key takeaways include:

- Deeper understanding of Django models and relationships  
- CRUD operations using Django Shell and QuerySets  
- Creating and validating manual and model-based forms  
- Using Django messages to provide UI feedback  
- Implementing user login, logout, and signup with session persistence  
- Class-Based Views (CBV) concepts: While not fully implemented in this specific project, I gained a strong theoretical understanding of CBVs for building more scalable and organized views.  
- Custom User Models: Explored moving beyond default Django User to implement authentication with email/phone numbers, and how to add additional user fields like pictures.  
- Slugs: Learned to implement slugs for creating clean, human-readable URLs for blog posts.  
- Comment Management: Implemented features for users to delete their own comments and ensured each blog post has its unique comment section.  
- Aggregate Functions: Used Django's aggregate functions to perform calculations, such as getting the total number of comments for a blog.  
- Django Signals: Discovered and utilized Django signals to automate tasks like sending welcome emails to newly registered users.  
- Faker Library: Practiced generating realistic fake data for development and testing purposes using the Faker library.  

---

🙌 **Credits & Resources**

- CodingForAll Django Playlist by Abhijeet Gupta  
- Telusko Django Playlist by Navin Reddy  
- Bootstrap 5 Documentation  
- ChatGPT – for guidance on code structure and Bootstrap help  

---

🧑‍💻 **Author**  
**Abbas Ali**  
[LinkedIn](https://www.linkedin.com/in/abbas-abro/) | [GitHub](https://github.com/abbasabro)
