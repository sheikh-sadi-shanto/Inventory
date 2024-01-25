from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import os
# Create your models here.


def validate_size(value):
    max_size=4*1024*1024
    file_size=value.size
    print('allow')
    if max_size<file_size:
        print('not allow')
        raise ValueError('this file is more than 4MB ')
    return value


class Category(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subcat=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Item(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='item_images')
    file=models.FileField(blank=True,null=True,upload_to='item_file',validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx']),validate_size])
    cta=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    stock=models.IntegerField(default=0)
    def __str__(self):
        return self.name


class SubItem(models.Model):
    subitem=models.ForeignKey(Item,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    stock=models.IntegerField(default=0)
    img=models.ImageField(upload_to='item_images')
    file=models.FileField(blank=True,null=True,upload_to='item_file',validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx']),validate_size])

    
    def __str__(self):
        return self.name

class Institute(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=300) 
    note=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Branch(models.Model):
    br=models.ForeignKey(Institute,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    note=models.CharField(max_length=300)
    def __str__(self):
        return self.name
    

class Department(models.Model):
    dep=models.ForeignKey(Branch,on_delete=models.CASCADE)
    name=models.CharField(max_length=300)
    note=models.CharField(max_length=300)
    def __str__(self):
        return self.name


class InventoryRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.CharField(max_length=300)
    subitem=models.CharField(max_length=300)
    quantity=models.IntegerField()
    note=models.CharField(max_length=300)
    dispersed=models.BooleanField(default=False)
    pur_dispersed=models.BooleanField(default=False)
    def __str__(self):
        return self.item



class PurchesOrder(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    note=models.CharField(max_length=300)
    # pur_branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    file=models.FileField(blank=True,null=True,upload_to='item_file',validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx']),validate_size])
    inv_req=models.ForeignKey(InventoryRequest,on_delete=models.CASCADE)

