from django import forms
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "last_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "email":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
        }


        
class ProForm(forms.ModelForm):
    class Meta:
        model=ProfilUpdate
        fields=["Image","Numer","Father_name","Class_Roll","Bed_Number","Blord_Group","Address","Parents_number","Date_of_Barth","Gender","Emediate_Gauedion_Numer"]
        widgets={
            "Image":forms.FileInput(attrs={"class":"form-control"}),
            "Numer":forms.TextInput(attrs={"class":"form-control"}),
            "Father_name":forms.TextInput(attrs={"class":"form-control"}),
            "Class_Roll":forms.TextInput(attrs={"class":"form-control"}),
            "Bed_Number":forms.TextInput(attrs={"class":"form-control"}),
            "Blord_Group":forms.Select(attrs={"class":"form-control"}),
            "Address":forms.TextInput(attrs={"class":"form-control"}),
            "Parents_number":forms.TextInput(attrs={"class":"form-control"}),
            "Date_of_Barth":forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            "Gender":forms.Select(attrs={"class":"form-control"}),
            "Emediate_Gauedion_Numer":forms.TextInput(attrs={"class":"form-control"}),
        }

class Avalavel(forms.ModelForm):
    class Meta:
        model=Afternoon_Meal
        fields=["Available"]