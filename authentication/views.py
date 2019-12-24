from django.shortcuts import render,redirect,get_list_or_404

# Create your views here.
def home(request):
    return render(request,'index.html')
