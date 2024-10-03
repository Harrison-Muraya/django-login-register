from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            # validate password
            if password != confirm_password:
                messages.error(request, 'password do not match')
                return redirect('register')
            
            user = User.objects.create_user(
                username= username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                password=password
            )
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to your post list or homepage after registration

        return render(request, 'register.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged In Welcome back')
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')