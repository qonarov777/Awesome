from django.shortcuts import render, redirect
from .models import Starthome, Startteam, Startportfolio, Startme
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def Indexview(request):
    
    starthome=Starthome.objects.all()
    startteam=Startteam.objects.all()
    startme=Startme.objects.all()
    startportfolio=Startportfolio.objects.all()
    context={
                'starthome':starthome, 
                'startteam':startteam,
                "startportfolio":startportfolio,
                'startme':startme
                   
                }
    
    return render(request,'index.html', context=context )

def Registerview(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, " Account created for" +  user)
            return redirect('login')
    context = { 'form' : form }
    
    return render(request, 'register.html', context=context )

def Loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request, 'Username or password is incorrect')
    context= { }
    
    return render(request, 'login.html', context=context)

def Logoutview(request):
    
    logout(request)
    
    return redirect('login')