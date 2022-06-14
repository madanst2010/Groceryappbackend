from django.contrib import admin
from .models import   User, Role, Department, Aisle, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['product_name']
    search_fields = ('product_name',)
    
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Aisle)
admin.site.register(Product,ProductAdmin)
