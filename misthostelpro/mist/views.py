from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from datetime import date
from .form import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        morinig_meal=Morning_Meal.objects.all()
        afternoon_meal=Afternoon_Meal.objects.all()
        denar_meal=Denar_Meal.objects.all()
        sendv={
            "morning":morinig_meal,
            "afternoon":afternoon_meal,
            "denar":denar_meal
        }
        return render(request,"index.html",sendv)
    return redirect(login)

def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"login.html",{'error':"Invalide User Password"})
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect(index)
def mealorder(request):
    Oname=request.POST.get("name")
    Oprice=request.POST.get("price")
    Oqun=request.POST.get("Quantity")
    Oid=request.POST.get("id")
    Odate=str(date.today())
    print(Oname,Oprice,Oqun,Oid,Odate)
    if request.method=="POST":
        order=Meal_Order(Name=request.user,Food_Name=Oname,Food_ID=Oid,Price=Oprice,Quantity=Oqun,Date_Time=Odate)
        order.save()
        return render(request,"index.html")
    return render(request,"index.html")
def confirm(request,id):
    qun=request.POST.get("qun")
    qunt=int(qun)
    if request.method=="POST":
        pk=Morning_Meal.objects.filter(pk=id)
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
        price=int(dam)*qunt
        send_item={
            'name':name,
            'id':fid,
            "price":price,
            "Quantity":qun
        }
    return render(request,"confirm.html",send_item)
def confirmlunch(request,id):
    qun=request.POST.get("qun")
    qunt=int(qun)
    if request.method=="POST":
        pk=Afternoon_Meal.objects.filter(pk=id)
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
        price=int(dam)*qunt
        send_item={
            'name':name,
            'id':fid,
            "price":price,
            "Quantity":qun
        }
    return render(request,"confirm.html",send_item)
def confirmdener(request,id):
    qun=request.POST.get("qun")
    qunt=int(qun)
    if request.method=="POST":
        pk=Denar_Meal.objects.filter(pk=id)
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
        price=int(dam)*qunt
        avalavle=pk.Available
        send_item={
            'name':name,
            'id':fid,
            "price":price,
            "Quantity":qun
        }
    pk=Denar_Meal.objects.filter(pk=1)
    print(int(avalavle))
    return render(request,"confirm.html",send_item)


def singup(request):
    f_name=request.POST.get("f_name")
    l_name=request.POST.get("l_name")
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    bio=request.POST.get("bio")
    if request.method=="POST":
        if passw==passw:
            try:
                user=User.objects.get(username=email)
                return render(request,"add.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                rfm=ProfilUpdate(Numer=bio)
                rfm.save()
                return render(request,"add.html",{'success':"user created successfully"})    
        else:
            return render(request,"add.html") 
    return render(request,"add.html") 


def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect(login)

def updateprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ufrom=UserForm(request.POST,instance=request.user)
            pfrom=ProForm(request.POST,request.FILES,instance=request.user.profilupdate)
            if ufrom.is_valid() and pfrom.is_valid():
                ufrom.save()
                pfrom.save()
                return render(request,"profile.html",{"error":"Profile Update successfully"})
        else:
            ufrom=UserForm(instance= request.user)
            pfrom=ProForm(instance= request.user.profilupdate)
        return render(request,"updateprofile.html",{"userfrom":ufrom,"profrom":pfrom})
    else:
        return redirect(login)

def panelhed(request):
    allorder=Meal_Order.objects.all()

    sendvar={
        "meal":Meal_Order,
    }
    return redirect(request,"panelhed.html",sendvar)