
from django.contrib import admin
from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from apk.views import *


urlpatterns = [

    path('catagorylist',CatagoryList.as_view()),
    path('catagorylist/<int:pk>',CatagoryList.as_view()),

    path('subcatagorylist',SubCatagoryList.as_view()),
    path('subcatagorylist/<int:pk>',SubCatagoryList.as_view()),

    path('itemlist',Itemlist.as_view()),
    path('itemlist/<int:pk>',Itemlist.as_view()),

    path('subitemlist',SubItemlist.as_view()),
    path('subitemlist/<int:pk>',SubItemlist.as_view()),

    path('institutelist',InstituteList.as_view()),
    path('institutelist/<int:pk>',InstituteList.as_view()),

    path('branchlist',BranchList.as_view()),
    path('branchlist/<int:pk>',BranchList.as_view()),

    path('departmentlist',DepartmentList.as_view()),
    path('departmentlist/<int:pk>',DepartmentList.as_view()),

    path('inventoryrequestlist',InventoryRequestList.as_view()),
    path('inventoryrequestlist/<int:pk>',InventoryRequestList.as_view()),

    path('purchesOrder',PurchesOrderView.as_view()),
    path('purchesOrder/<int:pk>',PurchesOrderView.as_view()),

    path('myinventory',MyInventoryView.as_view()),
]
