# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render ,redirect
from django.contrib import auth 
from users.models import User
from django.contrib import messages
from .forms import LoginForm , SignupForm
from django.views.decorators.csrf import csrf_exempt



#LOGIN 
@csrf_exempt
def login(request):
    
    if request.method == "POST" :
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request , username = username , password = password)
            if user is not None :
                auth.login(request, user)
                messages.success(request ,"welcome{}".format(user.username))
                return redirect("home")
            else:
                messages.warning(request ,"wrong username or password ")
                form = LoginForm()
                return render(request,"login.htm",{"form" : form})
        else: 
            messages.warning(request ,"Please Verify you credentials")
            form = LoginForm()
            return render(request,"login.htm",{"form" : form})
    else:
        form = LoginForm()
        return render(request,"login.htm" , {"form" : form})


def register(request):
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["password"]
                
            if User.objects.filter(username = username).exists():
                messages.warning(request,"this username exists")
                form = SignupForm()
                return render(request , "signup.htm" , {'form':form})
            
            if password != confirm_password:
                messages.error(request,"this email exists")
                form = SignupForm
                return render(request , "signup.htm", {'form':form})
            user = User.objects.create_user(username=username,first_name=first_name , last_name=last_name,password=password)
            user = auth.authenticate(request , username= username , password=password)
            messages.success(request , "think you for registration")
            return redirect("dashbord")
    else:
        form = SignupForm()
        return render(request,"signup.htm" , {"form" :form})

def logout(request):
    auth.logout(request)
    return redirect("home")

def dashbord(request):
    return render(request , 'home.htm')