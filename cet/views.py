from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/form')
        else:
            messages.info(request,'Invalid Credentials!')
            return redirect('/login')
    else:
        return render(request, 'index.html')


def form(request):
    return render(request, 'form.html')


def upload(request):
    return render(request, 'upload.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username=request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print('user k parameters variables me daal diya hoon')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save;
                print('User Created')
                return redirect('/form')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('/signup')
    else:
        return render(request, 'signup.html')
