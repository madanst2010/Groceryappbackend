from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, default=0)
    status = models.IntegerField(default=1)
    first_name = models.CharField(max_length=100)

# Role for every user 
# 0 = normal user 
# 1 = developer 
# 2 = managers 
# 3 = owner 
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField()


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100)

class Aisle(models.Model):
    aisle_id = models.AutoField(primary_key=True)
    aisle = models.CharField(max_length=200)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    aisle_id = models.ForeignKey(Aisle, models.DO_NOTHING)
    department_id = models.ForeignKey(Department, models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.CharField(max_length=200)
    

