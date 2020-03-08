from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm,ProfileForm,CommentsForm
from django.contrib.auth import login
from .models import Comments, Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    comments=Comments.objects.all()
    return render(request,'instagram/index.html',{"images":images,"comments":comments})

@login_required
def profile(request):
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    return render(request,'registration/profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})

def search_username(request):

    if 'name' in request.GET and request.GET["name"]:
        searched_name = request.GET.get("name")
        username = Profile.search_by_name(searched_name)
        message = f"{searched_name}"

        return render(request, 'search.html', {"message": message, "username": username})

    else:
        message = "Sorry, No one by this username"
        return render(request, 'instagram/search.html', {"message": message})
    
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
        return redirect('index')

    else:
        form = ImageForm()
        return render(request,'instagram/upload_image.html', {"form":form})
    
@login_required (login_url='/accounts/register/')          
def image_likes(request,id):
    image =  Image.get_single_photo(id)
    user = request.user
    user_id = user.id
    
    if user.is_authenticated:
    
        image.save()
        
    return redirect('index')


# def comments(request,id):
#     comments = Comments.get_comments(id)
#     number = len(comments   )
    
#     return render(request,'instagram/comments.html',{"comments":comments,"number":number})        

def add_comment(request,id):
    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('index')

    else:
        form = CommentsForm()
        return render(request,'instagram/add_comment.html',{"form":form,"image":image})  
    
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
        return redirect('profile')

    else:
        form = ProfileForm()
        return render(request,'registration/edit_profile.html',{"form":form})
    
    
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
        return redirect('index')

    else:
        form = ImageForm()
        return render(request,'instagram/new_post.html',{"form":form})
    

