from rest_framework import serializers
from apk.models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('id','name','img','file','stock',)

class SubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubItem
        fields=('id','name','img','file','stock',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields=('id','name',)




class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields=('id','name','note')



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=('id','name','location','note')



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('id','name','note')


class InventoryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('id','name','item','subitem','quantity','note','dispersed','pur_dispersed')


class PurchesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchesOrder
        fields=('id','item','quantity','note','file')