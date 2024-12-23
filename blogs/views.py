from django.shortcuts import render,HttpResponseRedirect
from .forms import  SingUpForm



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
    form=SingUpForm
    return render(request, 'blogs/singup.html',{'form':form})

#login
def user_login(request):
    return render(request, 'blogs/login.html')