from django.shortcuts import render,redirect
from .forms import CreateUser , LoginUser
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    form = CreateUser
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            password1 = request.POST.get('password2')
            password2 = request.POST.get('password2')
            user = authenticate(request,username=username,first_name=firstname,last_name=lastname,password1=password1,password2=password2)
            login(request,user)
            return redirect('home')
        else:
            return render (request,'register.html',{'form':form})
    else:
        
        return render (request,'register.html',{'form':form})
    
def signin(request):
    form = LoginUser()
    if request.method=='POST':
        form = LoginUser(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            form = LoginUser(request.POST)
            return render (request,'signup.html',{'form':form})
            
    else:
        return render (request,'login.html',{'form':form})
def home(request):
    return render(request,'home.html')