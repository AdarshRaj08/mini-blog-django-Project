from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/home.html')


# about 
def about(request):
    return render(request,'blog/about.html')


# Contact 
def contact(request):
    return render(request,'blog/contact.html')


# Dashboard
def dashboard(request):
    return render(request,'blog/dashboard.html')

# Logout
def user_logout(request):
    return render(request,'blog/logout.html')

# Login
def user_login(request):
    return render(request,'blog/login.html')

# Signup
def singup(request):
    return render(request,'blog/signup.html')