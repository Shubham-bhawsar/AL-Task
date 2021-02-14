from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from home.models import Person
from home.tasks import dataadd,coladd

# Create your views here.
def index(request):
    return(HttpResponse("Hii There"))

def loginfun(request):
    if(request.method=="POST"):
        email=request.POST.get('Email')
        passw=request.POST.get('pass')
        email=email.split('@')[0]
        username = authenticate(username=email, password=passw)
        if username is not None:
            login(request,username)
            print(request.user.password)
            return redirect('/')
    # A backend authenticated the credentials
        else:
            return redirect('login')
    # No backend authenticated the credentials
        
    return render(request,"login.html")

def dataad(request):
    if(request.method=="POST"):
        guid = request.POST.get("guid")
        first_name =request.POST.get("fname")
        last_name =request.POST.get('lname')
        email = request.POST.get('email')
        phone =request.POST.get('phone')
        person=Person(guid=guid,first_name=first_name,last_name=last_name,email=email,phone=phone)
        person.save()
        arr=[str(guid),str(first_name),str(last_name),str(email),str(phone)]
        dataadd.delay(arr,2)
        return(HttpResponse("Data Added"))

def colad(request):
    if(request.method=="POST"):
        cl1 = request.POST.get("cl1")
        cl2 =request.POST.get("cl2")
        cl3 =request.POST.get('cl3')
        cl4 = request.POST.get('cl4')
        cl5 =request.POST.get('cl5')
        arr=[str(cl1),str(cl2),str(cl3),str(cl4),str(cl5)]
        coladd.delay(arr)
        return(HttpResponse("Column Updated"))


