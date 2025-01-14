from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . form import RegistrationForm, FilterForm, PhotoUploadForm
from django.contrib.auth import authenticate, login as auth_login
from .models import Photo, Tag, Like, Profile, Subscriber
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse


def error_404(request, exception):
  return render(request, '404.html')

def home(request):
    form = FilterForm(request.GET or None)
    photos = Photo.objects.all()
    
    if form.is_valid():
        tag = form.cleaned_data.get('tag')
        if tag:
            photos = photos.filter(tags=tag)
            
    return render (request, 'home.html', {'form':form, 'photos':photos})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user  
            photo.save()
            form.save_m2m()    
            return redirect('home')  
    else:
        form = PhotoUploadForm()

    return render(request, 'upload_photo.html', {'form': form})

def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    
    if photo.user == request.user:
        photo.delete()
        return redirect('home')
    else:
        return redirect('home')

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        photo.likes += 1
        photo.save()
    return redirect('home')  

@login_required
def dislike_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        photo.dislikes += 1
        photo.save()
    return redirect('home') 


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'photo_detail.html', {'photo': photo})


@login_required
def filter_photos_by_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    photos = tag.photos.all()
    return render(request, 'home.html', {'photos': photos})

def gallery(request):
    tag = request.GET.get('tag')
    if tag:
        photos = Photo.objects.filter(tags__name__icontains=tag)
    else:
        photos = Photo.objects.all()
    
    tags = Tag.objects.all()
    context = {'photos': photos, 'tags': tags}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
    else:
       form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Credentials'
            return redirect('login')
    else:
        error_message = None
    return render(request, 'registration/login.html', {'error_message': error_message})

def user_logout(request):
    logout(request) 
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')
 
def update_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to update your profile.")
        return redirect('login') 

    user = request.user
    
    try:
        profile = user.profile 
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)  

    if request.method == 'POST':
        new_username = request.POST.get('new-username')
        new_email = request.POST.get('email')
        new_bio = request.POST.get('bio')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        
        if new_username:
            user.username = new_username
        
        
        if new_email:
            user.email = new_email
        
        
        if new_bio:
            profile.bio = new_bio  
        
        
        if new_password:
            if new_password == confirm_password:
                user.set_password(new_password)  
            else:
                messages.error(request, "Passwords do not match.")
                return redirect('update_profile')

        
        user.save()
        profile.save()  

        messages.success(request, "Profile updated successfully.")
        return redirect('profile')  

    return render(request, 'profile.html')  

def subscribe(request):
    if request.method =='POST':
        email = request.POST.get('email','')
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
           subscriber = Subscriber(email=email)
           subscriber.save()
           messages.success(request, 'Thank you for subscribing.')
           return redirect('subscribe')
    return render (request, 'subscribe.html')

def error_404(request, exception):
   return render(request, '404.html')