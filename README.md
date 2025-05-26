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
│
├── myblogpost/              # Main App
│   ├── models.py            # Blog Post model
│   ├── forms.py             # Manual and Model Forms
│   ├── views.py             # Views for auth & CRUD
│   ├── urls.py              # App-level URLs
│   ├── templates/           # All HTML templates
│   └── static/              # Static files (CSS, JS)
│
├── blogpost/                # Project config folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3               # Database file
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
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## 📚 What I Learned

- Deeper understanding of **Django models** and **relationships**
- CRUD operations using **Django Shell** and **QuerySets**
- Creating and validating **manual and model-based forms**
- Using **Django messages** to provide UI feedback
- Implementing **user login, logout, and signup** with session persistence

---

## 🙌 Credits & Resources

- [CodingForAll Django Playlist by Abhijeet Gupta]([https://www.youtube.com/playlist?list=PLgPJX9sVy92wDqVZ4F0PQ3vX_Gg6jG_9C](https://www.youtube.com/watch?v=Mezody4yiXw&list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk))
- Bootstrap 5 Documentation  
- ChatGPT – for guidance on code structure and Bootstrap help

---

## 🧑‍💻 Author

**Abbas Abro**  
[LinkedIn](https://www.linkedin.com/in/abro-abbas/) | [GitHub](https://github.com/abbasabro)
