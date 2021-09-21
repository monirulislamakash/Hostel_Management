from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('panelhead/', views.panelhed,name="panelhead"),
    path('confirm/<int:id>/',views.confirm,name="confirm"),
    path('confirmlunch/<int:id>/',views.confirmlunch,name="confirmlunch"),
    path('confirmdener/<int:id>/',views.confirmdener,name="confirmdener"),
    path('profile/',views.profile,name="profile"),
    path('updateprofile',views.updateprofile,name="updateprofile" ),
    path('singup/', views.singup,name="singup"),
    path('mealorder/', views.mealorder,name="mealorder"),
]