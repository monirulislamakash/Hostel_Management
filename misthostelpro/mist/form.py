from django import forms
from django.contrib.auth.models import User
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
        fields=["Image","Numer","Room_Number","Father_name","Class_Roll","Bed_Number","Blord_Group","Address","Parents_number","Date_of_Barth","Gender","Emediate_Gauedion_Numer"]
        widgets={
            "Numer":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Room_Number":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Father_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Class_Roll":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Bed_Number":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Blord_Group":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Address":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Parents_number":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Date_of_Barth":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Gender":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Emediate_Gauedion_Numer":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
        }
