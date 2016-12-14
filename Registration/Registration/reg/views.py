from django.shortcuts import render

from django.views.generic import TemplateView
from django.template import loader, Context
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from . import models

from reg.models import Registern
from reg.models import car_info
# Create your views here.



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

    
    
class First1(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'First.html', context=None)    
    
    
    

def demo(request):
    n = request.POST.get("Name",' ')
    u = request.POST.get("UName",' ')
    p = request.POST.get("Password",' ')
    r = request.POST.get("CPassword",' ')
    
    

#search = car_info(Name)
    queryset1 = models.Registern(Name=n, Username=u, Password=p,CPassword=r)
    

    queryset1.save()
    
    data = {
        'queryset1': queryset1,

    }
   
    return render(request, './Registration.html', data)


def archive(request):
    posts = models.Registern.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

def archive1(request):
    ln = request.POST.get("lname",' ')
    lp = request.POST.get("lpwd",' ')  
    posts = models.Registern.objects.all() 

    for post in posts:
    
    
     if ln==post.Username and lp==post.Password:
        return render(request, './home.html')
    else:
        return render(request,'./login.html')
  
        
def Reg(request): 
        return render(request, './Registration.html')
    
def prin(request):
    postss = models.Registern.objects.all() 
    for ppost in postss:
      return HttpResponse(ppost.Username)
  
def car(request):
    n = request.POST.get("loc_id",' ')
    print(n)
    ad = request.POST.get("from_id",' ')
    print(ad)
    em = request.POST.get("to_id",' ')
    print(em)
    

#search = car_info(Name)
    queryset1 = models.car_info(location=n, from_id=ad, to=em)
    

    queryset1.save()
    
    data = {
        'queryset1': queryset1,

    }
   
    return render(request, './home.html', data)    

def success(request):
    posts = models.car_info.objects.all()
    t = loader.get_template("SuccesfulB.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))


        
def book(request): 
        return render(request, './home.html')
    
def logout(request): 
        return render(request, './login.html')    
