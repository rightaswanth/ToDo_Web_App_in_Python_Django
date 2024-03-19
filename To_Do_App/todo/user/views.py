
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout


def home(request):
    return render(request,'home.html')


def login_view(request):
    error_message=None
    if request.POST:
        Username=request.POST['username']
        Password=request.POST['password']
        user=authenticate(username=Username,password=Password)
        if user:
            authlogin(request,user)
            # print(user)
            return redirect('task')
        else:
            error_message="Inavalid Credential"
    return render(request,'login.html',{'error_message':error_message})

def register_view(request):
    user=None
    if request.POST:
        Username=request.POST['username']
        Password=request.POST['password']
        Email=request.POST['email']

        print(Username,Password)
        user=User.objects.create_user(username=Username,password=Password,email=Email)
        return redirect('login')
    return render(request,'register.html',{'user':user})



def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the login page after logout

