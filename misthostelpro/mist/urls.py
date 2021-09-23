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
    path('delete/<int:id>/',views.delete,name="delete" ),
    path('mealhiostry/', views.mealhiostry,name="mealhiostry"),
    path('hostelmeal1/', views.hostelmeal1,name="hostelmeal1"),
    path('hostelmeal2/', views.hostelmeal2,name="hostelmeal2"),
    path('hostelmeal3/', views.hostelmeal3,name="hostelmeal3"),
    path('hostelmeal4/', views.hostelmeal4,name="hostelmeal4"),
    path('hostelmeal5/', views.hostelmeal5,name="hostelmeal5"),
    path('hostelmeal6/', views.hostelmeal6,name="hostelmeal6"),
    path('hostelmeal7/', views.hostelmeal7,name="hostelmeal7"),
]