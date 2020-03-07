from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images=Image.objects.all()
    return render(request,'instagram/index.html',{"images":images})

@login_required
def profile(request):
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    return render(request,'instagram/profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})
        
