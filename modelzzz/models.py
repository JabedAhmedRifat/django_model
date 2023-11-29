from django.db import models

class AppSetting(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    tag_line = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    footer = models.TextField()
    logo = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)





class Permission(models.Model):
    name = models.CharField(max_length=255 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now =True)





class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
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
    designationId = models.ForeignKey(Designation, on_delete=models.CASCADE)
    
    

    
    
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
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class Product_category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ProductSubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    product_category = models.ForeignKey(Product_category)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class ProductBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color_code = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    product_thumbnail = models.URLField(blank=True)
    product_subcategory = models.ForeignKey(ProductSubCategory)
    product_brand_id = models.ForeignKey(ProductBrand)
    description = models.TextField()
    sku = models.CharField(max_length=255 , unique=True)
    product_quantity = models.FloatField()
    product_sale_price = models.FloatField()
    product_purchase_price = models.FloatField()
    unit_type = models.TextField()
    unit_measurement = models.doubleField()
    reorder_quantity = models.IntegerField()
    product_vat =models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purchase_invoice_id = models.ForeignKey(AdjustInvoice,on_delete=models.CASCADE)





class ProductColor(models.Model):
    product = models.ForeignKey(Product)
    color = models.ForeignKey(Color)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class ProductVat(models.Model):
    title = models.CharField(max_length=255)
    parcentage = models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AdjustInvoiceProduct(models.Model):
    AdjustInvoice = models.ForeignKey(AdjustInvoice,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product)
    adjustQuantity = models.IntegerField()
    adjustType = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    



class Coupon(models.Model):
    code = models.TextField()
    type = models.TextField()
    value = models.FloatField()
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Customer(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    address = models.TextField()
    password = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CustomerPermission(models.Model):
    user = models.ForeignKey(User)
    permissions = models.ForeignKey(Permission, on_delete=models.CASCADE)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class Email(models.Model):
    senderEmail = models.TextField()
    receiverEmail = models.TextField()
    subject = models.TextField()
    body = models.TextField()
    emailStatus = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class EmailConfig(models.Model):
    email_config_name = models.TextField()
    email_host = models.TextField()
    email_port = models.IntegerField()
    email_user = models.TextField()
    email_pass = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class Migraiton(models.Model):
    migration = models.TextField()
    batch = models.IntegerField()





class PageSize(models.Model):
    page_size_name = models.TextField()
    width = models.FloatField()
    height = models.FloatField()
    unit = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)





class PersonalAccessToken(models.Model):
    tokenable_type = models.TextField()
    tokenable_id = models.ForeignKey()--------------
    token = models.ForeignKey()--------------
    abilities = models.TextField()
    last_used_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.TextField()
    address = models.TextField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PurchaseInvoice(models.Model):
    date = models.DateTimeField()
    total_amount = models.FloatField()
    discount = models.FloatField()
    paid_amount = models.FloatField()
    due_amount = models.FloatField()
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    note = models.TextField()
    supplier_memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PurchaseInvoiceProduct(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    product_purchase_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class PurchaseReorderInvoice(models.Model):
    reorder_invoice = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class ReturnPurchaseInvoice(models.Model):
    date = models.DateTimeField()
    total_amount = models.FloatField()
    note = models.TextField()
    purchase_invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReturnPurchaseInvoiceProduct(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice, on_delete=models)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    product_purchase_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class SaleInvoice(models.Model):
    date = models.DateTimeField()
    total_amount = models.FloatField()
    discount = models.FloatField()
    paid_amount = models.FloatField()
    due_amount = models.FloatField()
    profit = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    address = models.TextField()
    orderStatus = models.TextField()
    isHold = models.BooleanField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class SaleInvoiceProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    product_sale_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SaleInvoiceVat(models.Model):
    invoice = models.ForeignKey(SaleInvoiceProduct, on_delete=models.CASCADE)
    productVat = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ReturnSaleInvoice(models.Model):
    date = models.DateTimeField()
    total_amount = models.FloatField()
    note = models.TextField()
    sale_invoice = models.ForeignKey(SaleInvoiceProduct, on_delete=models.CASCADE)
    status  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class ReturnSaleInvoiceProduct(models.Model):
    invoice = models.ForeignKey(SaleInvoiceProduct, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    product_sale_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ReviewRating(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Shift(models.Model):
    name = models.CharField(max_length=255)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    workhour = models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubAccount(models.Model):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Quote(models.Model):
    quote_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_name = models.CharField(max_length=255)
    quote_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    terms_and_conditions = models.TextField()
    description = models.TextField()
    discount = models.FloatField()
    total_amount = models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class QuotaProduct(models.Model):
    quota = models.ForeignKey(Quote, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    product_quantity = models.FloatField()
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
