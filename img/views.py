from img.models import Github
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
import requests
from bs4 import BeautifulSoup as bs
def index(request):
    if request.method == 'POST':
        github_user = request.POST['github_user']
        url = 'https://github.com/'+github_user
        r = requests.get(url)
        soup = bs(r.content)
        profile = soup.find('img', {'alt' : 'Avatar'})['src']
        new_github_user = Github(
            githubuser = github_user,
            imagelink = profile
        )
        new_github_user.save()
        messages.info(request, 'User '+ github_user +' Image Saved')
        return redirect('/')
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username = username).first():
            messages.warning(request, 'username already exist')
            return redirect('register')
        if User.objects.filter(email = email).first():
            messages.warning(request, 'email already exist')
            return redirect('register')
        if password == password2:
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            return redirect('login')
        else:
            messages.warning(request, 'password dont match')
            return redirect('register')
    return render(request, 'signup.html')
def logindef(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.warning(request, 'user not found')
            return redirect('login')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.warning(request, 'passowrd is incorrect')
            return redirect('login')
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')
def logoutdef(request):
    auth.logout(request)
    return redirect('login')
    image = Github.objects.filter(id= id)
    return render(request, 'images.html', {'image':image})
