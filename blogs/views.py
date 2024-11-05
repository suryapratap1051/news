from django.shortcuts import render,HttpResponseRedirect


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
def singup(request):
    return render(request, 'blogs/singup.html')

#login
def user_login(request):
    return render(request, 'blogs/login.html')