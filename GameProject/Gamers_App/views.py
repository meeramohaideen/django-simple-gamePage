from django.shortcuts import render
from django.views.generic import View,TemplateView
from .forms import UserRegisterForm,UserLoginForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
class IndexView(TemplateView):
    template_name = "Gamers_App/Gamers_MainPage.html"



def loginPage(request):


    if request.method=='POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print (user)

        if user:
            login(request,user)
            print("loggedin")
            return HttpResponseRedirect(reverse('indexView'))
        else:
            print(username,password)
            user = authenticate(username='username', password='password')
            print(user)
            return HttpResponse("Login Failed")
    else:
        return render(request,'Gamers_App/Gamers_login.html')

@login_required()
def userLogout(request):
    logout(request)
    print("loggedout")
    return HttpResponseRedirect(reverse('indexView'))
