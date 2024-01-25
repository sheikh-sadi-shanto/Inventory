from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from apk.models import *
from apk.serializer import *
# Create your views here.


class CatagoryList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=Category.objects.get(id=pk)
            serializers=CategorySerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=Category.objects.all()
        serializers=CategorySerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)

class SubCatagoryList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=SubCategory.objects.get(id=pk)
            serializers=SubCategorySerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=SubCategory.objects.all()
        serializers=SubCategorySerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=SubCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    

class Itemlist(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=Item.objects.get(id=pk)
            serializers=ItemSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=Item.objects.all()
        serializers=ItemSerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=ItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    

class SubItemlist(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=SubItem.objects.get(id=pk)
            serializers=SubItemSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=SubItem.objects.all()
        serializers=SubItemSerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=SubItemSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    






class InstituteList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=Institute.objects.get(id=pk)
            serializers=InstituteSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=Institute.objects.all()
        serializers=InstituteSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=InstituteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    


class BranchList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=Branch.objects.get(id=pk)
            serializers=BranchSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=Branch.objects.all()
        serializers=BranchSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=BranchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)




class DepartmentList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=Department.objects.get(id=pk)
            serializers=DepartmentSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=Department.objects.all()
        serializers=DepartmentSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=DepartmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    


class InventoryRequestList(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=InventoryRequest.objects.get(id=pk)
            serializers=InventoryRequestSerializer(queryset,many=False)
            return Response(serializers.data)

        queryset=InventoryRequest.objects.all()
        serializers=InventoryRequestSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=InventoryRequest(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)