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
                return render(request,"login.htm",{})
        else: 
            messages.warning(request ,"Please Verify you credentials")
            form = LoginForm()
            return render(request,"login.htm",{"form" : form})
    else:
        form = LoginForm()
        return render(request,"login.htm" , {"form" : form})


def register(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if User.objects.filter(username = username).exists():
            messages.warning(request,"this username exists")
            return render(request , "register.htm")
        if User.objects.filter(email = email).exists():
            messages.error(request,"this email exists")
            return render(request , "register.htm")
        if password != confirm_password:
            messages.error(request,"this email exists")
            return render(request , "register.htm")
        
        user = User.objects.create_user(username , email = email , password=password, is_staff= True , is_superuser = True)
        user = auth.authenticate(request , username= username , password=password)
        messages.success(request , "think you for registration")
        return redirect("home")
    else:
        form = SignupForm()
        return render(request,"signup.htm")

def logout(request):
    auth.logout(request)
    return redirect("home")