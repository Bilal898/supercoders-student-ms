from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from student_management_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages

# from channels.auth import login
# Create your views here.



def showDemoPage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h4>Method not allowed</h4>")
    else:
        # user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        user = authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/admin_home")
            # return HttpResponse("Email: "+ request.POST.get("email") + "Password: "+ request.POST.get("password"))
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("user: " + request.user.email + " usertype: "+request.user.user_type)
    else:
        return HttpResponse("please login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")