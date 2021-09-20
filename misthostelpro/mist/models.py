from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your models here.
class Morning_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    def __str__(self):
        return self.Name
class Afternoon_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    def __str__(self):
        return self.Name
class Denar_Meal(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Available=models.CharField( max_length=10,default="")
    def __str__(self):
        return self.Name
class Meal_Order(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,default="")
    Food_Name=models.CharField(max_length=50,default="")
    Food_ID=models.CharField(max_length=50,default="")
    Price=models.CharField(max_length=50,default="")
    Quantity=models.CharField(max_length=10,default="")
    Date_Time=models.CharField(max_length=50,default="")
    def __str__(self):
        return str(self.Name)
class ProfilUpdate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Image=models.ImageField(upload_to="static/profile/pic/",default="static/profile/avatar.png")
    Numer=models.TextField(default="Enter Phone Number")
    Room_Number=models.CharField(max_length=10,default="00")
    Father_name=models.CharField(max_length=50,default="Need to Enter")
    Class_Roll=models.CharField(max_length=50,default="Need to Enter")
    Bed_Number=models.CharField(max_length=10,default="00")
    Blord_Group=models.CharField(max_length=2,default="+-")
    Address=models.CharField(max_length=300,default="Need to Enter")
    Parents_number=models.CharField(max_length=15,default="Need to Enter")
    Date_of_Barth=models.CharField(max_length=30,default="Need to Enter")
    Gender=models.CharField(max_length=13,default="Need to Enter")
    Emediate_Gauedion_Numer=models.CharField(max_length=15,default="Need to Enter")
    MealBill=CharField(max_length=10,default="000")
    def __str__(self):
        return str(self.user)