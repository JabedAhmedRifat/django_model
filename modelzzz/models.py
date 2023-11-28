from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Designation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    salary = models.IntegerField()
    idNo = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bloodGroup = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    joinDate = models.DateField(auto_now_add=True)
    leaveDate = models.DateField(auto_now=True)
    status = models.CharField(max_length=255)
    roleId = models.ForeignKey(on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    designationId = models.ForeignKey(on_delete=models.CASCADE)
    
    
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Account(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    debit_id = models.ForeignKey()-------------------
    credit_id = models.ForeignKey()-----------------
    particular = models.CharField(max_length=255)
    amount = models.FloatField(max_length=255)
    type = models.CharField(max_length=255)
    related_id = models.IntegerField()
    status = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AdjustInvoice(models.Model):
    note = models.CharField(max_length=255)
    user_id = models.ForeignKey(User)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_thumbnail = models.URLField(blank=True)
    product_subcategory = models.ForeignKey()-----------
    product_brand_id = models.ForeignKey()
    



class AdjustInvoiceProduct(models.Model):
    AdjustInvoice_id = models.ForeignKey(AdjustInvoice)
    product_id = models.ForeignKey(Product)---------
    adjustQuantity = models.IntegerField()
    adjustType = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    


    