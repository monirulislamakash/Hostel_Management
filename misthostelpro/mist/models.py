from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import date
# Create your models here.
class Morning_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    When=models.CharField("Breakfast",max_length=30,default="Breakfast")
    def __str__(self):
        return self.Name
class Afternoon_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    When=models.CharField("Lunch",max_length=30,default="Lunch")
    def __str__(self):
        return self.Name
class Denar_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    When=models.CharField("Dinner",max_length=30,default="Dinner")
    def __str__(self):
        return self.Name
class Meal_Order(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Roll=models.CharField(max_length=50,default="")
    Hostel=models.CharField(max_length=13,default=1)
    Room_Number=models.CharField(max_length=13,default='')
    Food_Name=models.CharField(max_length=50,default="")
    Food_ID=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Quantity=models.CharField(max_length=10,default="")
    Date_Time=models.CharField(max_length=50,default="")
    When=models.CharField(max_length=30,default="Breakfast")
    def __str__(self):
        return str(self.Name)+"  ||  "+str(self.When)+"  ||  "+str(self.Date_Time)
class Demo(models.Model):
    Name=models.CharField(max_length=50,default="")
    Roll=models.CharField(max_length=50,default="")
    Hostel=models.CharField(max_length=13,default=1)
    Room_Number=models.CharField(max_length=13,default='')
    Break_qun=models.IntegerField(max_length=50,default=0)
    Break=models.CharField(max_length=50,default="")
    Break_price=models.IntegerField(max_length=50,default=0)
    Lunch_qun=models.IntegerField(max_length=50,default=0)
    Lunch=models.CharField(max_length=50,default="")
    Lunch_price=models.IntegerField(max_length=50,default=0)
    Denar_qun=models.IntegerField(max_length=50,default=0)
    Denar=models.CharField(max_length=50,default="")
    Denar_price=models.IntegerField(max_length=50,default=0)
    Date_Time=models.CharField(max_length=50,default=date.today())
    def __str__(self):
        return str(self.Name)+"  ||  "+str(self.Date_Time)
class ProfilUpdate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    StudentName=CharField(max_length=100,default='')
    Hostel=models.CharField(max_length=13,default=1)
    Image=models.ImageField(upload_to="static/profile/pic/",default="static/profile/avatar.png")
    Numer=models.IntegerField(default=+880)
    Room_Number=models.CharField(max_length=10,default="00")
    Father_name=models.CharField(max_length=50,default="Need to Enter")
    Father_profession=models.CharField(max_length=100,default="Need to Enter")
    Class_Roll=models.CharField(max_length=50,default="Need to Enter",unique=True)
    Bed_Number=models.CharField(max_length=10,default="00")
    selectblord=(
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('O-','O-'),
        )
    Blood_Group=models.CharField(max_length=5,choices=selectblord,default="+-")
    Address=models.CharField(max_length=300,default="Need to Enter")
    Parents_number=models.CharField(max_length=15,default="Need to Enter")
    Date_of_Birth=models.CharField(max_length=30,default="Need to Enter")
    selectgender=(
        ('male','Male'),
        ('female','Female')
        )
    Gender=models.CharField(max_length=10,choices=selectgender,default="Male")
    Emediate_Gauedion_Numer=models.CharField(max_length=15,default="Need to Enter")
    MealBill=CharField(max_length=10,default="000")
    permission=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)
class All_Meal_Order(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Hostel=models.CharField(max_length=13,default=1)
    Food_Name=models.CharField(max_length=50,default="")
    Food_ID=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Quantity=models.CharField(max_length=10,default="")
    Date_Time=models.CharField(max_length=50,default="")
    When=models.CharField(max_length=30,default="breakfast")
    def __str__(self):
        return str(self.Name)
class Notice(models.Model):
    Athor=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Titel=models.CharField(max_length=50,default="")
    Body=models.TextField()
    Date=models.DateField(default=date.today())
    def __str__(self):
        return str(self.Athor)+'|'+str(self.Date)
class Payment_History(models.Model):
    User=models.CharField(max_length=100)
    Name=models.CharField(max_length=100,default="")
    Mobile=models.IntegerField(max_length=50,default= +880)
    Fixed=models.IntegerField(max_length=50,default=0)
    Food=models.IntegerField(max_length=50,default=0)
    Pledge=models.IntegerField(max_length=50,default=0)
    Development=models.IntegerField(max_length=50,default=0)
    Receiver=models.CharField(max_length=100,default="")
    Amount=models.IntegerField(max_length=50,default=0)
    Date=models.DateField(default=date.today())
    def __str__(self):
        return str(self.Name)+'  ||  '+str(self.Resiver)+'  ||  '+str(self.Date)