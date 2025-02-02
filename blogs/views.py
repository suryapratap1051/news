from django.shortcuts import render,HttpResponseRedirect
from .forms import  SingUpForm ,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



#home
def home(request):
    return render(request, 'blogs/home.html')

#about
def about(request):
    return render(request, 'blogs/about.html')

#contect
def contect(request):
    return render(request, 'blogs/contect.html')

#deshboard
def deshboard(request):
    return render(request, 'blogs/deshboard.html')

#Logout
def user_logout(request):
    return HttpResponseRedirect ('/')
    

#singup
def user_singup(request):    
    if request.method =="POST":           
       form=SingUpForm(request.POST)
       if form.is_valid():
           messages.success(request,'congratulations! you have become on Author')           
           form.save()
    else:               
        form=SingUpForm
    return render(request, 'blogs/singup.html',{'form':form})

#login
def user_login(request):
    
   if not request.user.is_authenticated:
    if request.method =="POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname= form.cleaned_data['username']
            upass= form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login successfully')
                return HttpResponseRedirect('/deshboard/')
    else:
        form=LoginForm()
    return render(request, 'blogs/login.html', {'form': form})
   else:
    return HttpResponseRedirect('/deshboard')