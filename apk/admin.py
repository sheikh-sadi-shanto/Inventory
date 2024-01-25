from django.contrib import admin
from apk.models import *
# Register your models here.

admin.site.register(Item)
admin.site.register(SubItem)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Institute)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(InventoryRequest)