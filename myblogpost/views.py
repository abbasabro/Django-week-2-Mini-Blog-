from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from .models import *
# Create your views here.
def index(request):
    return render(request , 'index.html')

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not User.objects.filter( username = username ).exists():
                messages.info(request , "Invalid Username")
            
            user = authenticate(username = username , password = password)

            if user is None:
                messages.info(request , "Invalid Password")
            else:
                login(request , user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form' : form
    }
    return render(request , 'login.html' , context)

def logout_page(request):
    logout(request)
    return redirect('login_page')

def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter( username = username ).exists():
                messages.info(request , "Username Already Taken")

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name ,
                username = username 
            )
            user.set_password(password)
            user.save()
            messages.success(request,  "Account Created SuccessFully")
            return redirect("registration_page")       
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request , 'registration.html',context)

@login_required(login_url="/login/")
def home(request):
    post = Post.objects.all()
    if request.GET.get('search'):
        post = post.filter(title__icontains = request.GET.get('search'))
    context  = {'posts':post}
    return render(request , 'home.html',context)

@login_required(login_url="/login/")
def addblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.user = request.user
            blogpost.save()
            messages.success(request,"Post Created Successfully")
            return redirect("addblog")
    else:
        form = BlogForm()
    context  = {'form' : form}
    return render(request , 'addblog.html',context)

@login_required(login_url="/login/")
def myblog(request):
    queryset = Post.objects.filter(user=request.user)
    context  = {'posts':queryset}
    return render(request , 'myblog.html',context)

@login_required(login_url="/login/")
def updateblog(request , id):
    queryset = Post.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES , instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request,"Post Updated Successfully")
            return redirect("myblog")
    else:
        form = BlogForm(instance=queryset)
    context  = {'form' : form}
    return render(request , 'updateblog.html',context)

@login_required(login_url="/login/")
def deleteblog(request , id):
    queryset = Post.objects.get(id=id)
    messages.warning(request , "Post deleted succesfully ")
    queryset.delete()
    return redirect("myblog")

@login_required(login_url="/login/")
def postdetail(request , id):
    queryset = Post.objects.get(id=id)
    context = {'post':queryset}
    return render(request , 'post_detail.html' , context)