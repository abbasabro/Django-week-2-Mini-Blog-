"""
URL configuration for BlogPost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from myblogpost.views import *

urlpatterns = [
    path('',index,name="index"),
    path('home/',home,name="home"),
    path('add-blog/',addblog,name="addblog"),
    path('my-blog/',myblog,name="myblog"),
    path('update-blog/<id>/',updateblog,name="updateblog"),
    path('delete-blog/<id>/',deleteblog,name="deleteblog"),
    path('post-detail/<id>/',postdetail,name="postdetail"),
    path('registration/',registration_page,name="registration_page"),
    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name="logout_page"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns +=  staticfiles_urlpatterns()
    
