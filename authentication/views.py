from django.shortcuts import render,redirect,get_list_or_404
import pyrebase


# Create your views here.
def home(request):
    return render(request,'index.html')


    config = {
    'apiKey': "AIzaSyC0Ba-3qLhzi8hwxVGYRIM2c1WVpmanmzc",
    'authDomain': "cpanel-5e873.firebaseapp.com",
    'databaseURL': "https://cpanel-5e873.firebaseio.com",
    'projectId': "django-authentication-9552d",
    'storageBucket': "http://django-authentication-9552d.appspot.com/",
    'messagingSenderId': "624344477485"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "CREDENTIALS ERROR!"
    return render(request,"signIn.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})
