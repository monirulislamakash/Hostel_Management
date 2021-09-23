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
        appstortitel=Meal_Order.objects.filter(Name__icontains=request.user)
        
        appstor=appstortitel
        sendv={
            "morning":morinig_meal,
            "afternoon":afternoon_meal,
            "denar":denar_meal,
            "todyfood":appstor,
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
        order=Meal_Order(Name=request.user,Hostel=request.user.profilupdate.Hostel,Food_Name=Oname,Food_ID=Oid,Price=Oprice,Quantity=Oqun,Date_Time=Odate)
        allorder=All_Meal_Order(Name=request.user,Food_Name=Oname,Food_ID=Oid,Price=Oprice,Quantity=Oqun,Date_Time=Odate)
        order.save()
        allorder.save()
        return redirect(index)
    return redirect(index)
def confirm(request,id):
    qun=request.POST.get("qun")
    qunt=int(qun)
    if request.method=="POST":
        pk=Morning_Meal.objects.filter(pk=id)
    #Price counter Meal####################
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
        price=int(dam)*qunt
    #Available Meal####################
        for i in pk:
            ava=i.Available
            aval=int(ava)-int(qunt)
        t = Morning_Meal.objects.get(id=id)
        t.Available = aval
        t.save()
    #Meal Bill################################
        mealbillMinus=ProfilUpdate.objects.filter(user=request.user)
        for i in mealbillMinus:
            mealardam=i.MealBill
            dam=int(mealardam)-int(price)
        mealbill=ProfilUpdate.objects.get(user=request.user)
        mealbill.MealBill = dam
        mealbill.save()
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
    #Price counter Meal####################
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
        price=int(dam)*qunt
    #Available Meal####################
        for i in pk:
            ava=i.Available
            aval=int(ava)-int(qunt)
        t = Afternoon_Meal.objects.get(id=id)
        t.Available = aval
        t.save()
    #Meal Bill################################
        mealbillMinus=ProfilUpdate.objects.filter(user=request.user)
        for i in mealbillMinus:
            mealardam=i.MealBill
            dam=int(mealardam)-int(price)
        mealbill=ProfilUpdate.objects.get(user=request.user)
        mealbill.MealBill = dam
        mealbill.save()
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
    #Price counter Meal####################
        for i in pk:
            name=i.Name
            dam=i.Price
            fid=i.id
    #Available Meal####################
        for i in pk:
            ava=i.Available
            aval=int(ava)-int(qunt)
        t = Denar_Meal.objects.get(id=id)
        t.Available = aval
        t.save()
        price=int(dam)*qunt
        #Meal Bill################################
        mealbillMinus=ProfilUpdate.objects.filter(user=request.user)
        for i in mealbillMinus:
            mealardam=i.MealBill
            dam=int(mealardam)-int(price)
        mealbill=ProfilUpdate.objects.get(user=request.user)
        mealbill.MealBill = dam
        mealbill.save()
        send_item={
            'name':name,
            'id':fid,
            "price":price,
            "Quantity":qun
        }
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
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.all()
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)

def delete(request,id):
    if request.method=="POST":
        pk=Meal_Order.objects.get(pk=id)
        pk.delete()
        return redirect(panelhed)
def mealhiostry(request):
    allmeal=All_Meal_Order.objects.filter(Name__icontains=request.user)
    sendvar={
        "allmeal":allmeal
    }
    return render(request,"allmeal.html",sendvar)
#hostel##################################
def hostelmeal1(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=1)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal2(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=2)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal3(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=3)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal4(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=4)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal5(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=5)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal6(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=6)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)
#hostel##################################
def hostelmeal7(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            allorder=Meal_Order.objects.filter(Hostel=7)
            sendvar={
                "meal":allorder,
            }
            return render(request,"panelhed.html",sendvar)
        return redirect(index)
    return redirect(login)