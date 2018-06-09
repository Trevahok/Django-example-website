from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import User
# Create your views here.
def login(request):
    _username='404'
    if request.method=='GET':
        return render(request,'login/login.html',{'user':''})
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(pk=username)
        except User.DoesNotExist:
            return render(request,'login/login.html',{'user':_username})
        else:
            if user.password==password:
                _username=username
                return render(request,'alwin/home.html',{'user':_username})
