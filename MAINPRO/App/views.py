from django.shortcuts import render,redirect
from django.http import HttpResponse
# from App.models import signuppage
# from App.forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')




def signup(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            cpassword=request.POST.get('cpassword')
            if password==cpassword:
                if User.objects.filter(username=name,email=email).exists():
                    messages.info(request,'user already exists')
                    print('Already have')
                else:
                    new = User.objects.create_user(username=name,password=password,email=email)
                    new.set_password(password)
                    new.save()
                    return home(request)
            else:
                print("Wrong password")
        return render(request,'signup.html')


# def signup(request):
#     if (request.method =='POST'):
#         a = request.POST['name']
#         b =request.POST['email']
#         c = request.POST['phoneno']
#         d = request.POST['password1']
#         e = request.POST['password2']
#         user = signuppage.objects.create(username = a,email = b,phoneno = c,password1 = d,password2 =e)
#         user.save()
#         return home(request)
#     return render(request,'signup.html')
    

def user_login(request):
    if(request.method=="POST"):
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("User Not Found!!")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return user_login(request)



