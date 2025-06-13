from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login , logout
from .models import *
from django.core.paginator import Paginator 
User = get_user_model()
from myblogpost.seed import *
from django.db.models import *
from django.views.generic.edit import FormView
# Create your views here.
def index(request):
    return render(request , 'index.html')

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if not User.objects.filter( email = email ).exists():
                messages.info(request , "Invalid Email address")
            
            user = authenticate( email = email , password = password)

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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter( email = email ).exists():
                messages.info(request , "Username Already Taken")

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name ,
                email = email 
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
        post = post.filter(
            Q(title__icontains = request.GET.get('search'))|
            Q(content__icontains = request.GET.get('search'))|
            Q(user__first_name__icontains = request.GET.get('search'))
              )
    paginator = Paginator(post, 5)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context  = {'posts':post , "page_obj": page_obj}
    return render(request , 'home.html',context)

@login_required(login_url="/login/")
def addblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.user = request.user
            blogpost.slug = generate_slug(blogpost.title) 
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
def updateblog(request , slug):
    queryset = Post.objects.get(slug=slug)
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
def user_info(request):
    info   = request.user
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == "profile_pic_form":
            profile_pic = request.FILES.get('profile_pic')
            if profile_pic:
                info.profile_pic = profile_pic
                info.save()
                messages.success(request, "Profile picture updated successfully.")
            else:
                messages.error(request, "Please Upload the pic")

        elif form_type == "user_info_form":
            first_name  = request.POST.get('first_name')
            last_name  = request.POST.get('last_name')
            phone_no  = request.POST.get('phone_no')

            info.first_name = first_name
            info.last_name = last_name
            info.phone_no = phone_no

            info.save()

            messages.success(request , "Information Update Succesfully")
        
    context = {'info' : info}
    return render(request , 'user_info.html' , context)
@login_required(login_url="/login/")
def postdetail(request , slug):
    queryset = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = queryset
            comment.user = request.user
            comment.save()
            messages.success(request,"Comment Successfully")
            return redirect("postdetail" , slug)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post =queryset)
    total_comments = Comment.objects.filter(post__slug=slug).count()
    context = {'post':queryset ,'form' : form , 'comments' : comments , 'total_comments' : total_comments}
    return render(request , 'post_detail.html' , context )

@login_required(login_url="/login/")
def deletecomment(request, post_slug, id):
    try:
        post = Post.objects.get(slug=post_slug)
    except:
        return HttpResponseNotFound("Post not found")
    queryset = Comment.objects.get(id=id , post = post)
    queryset.delete()
    return redirect('postdetail' , slug = post_slug)

