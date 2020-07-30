from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Carrier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    buy_price = models.DecimalField(max_digits=9, decimal_places=2)
    sell_price = models.DecimalField(max_digits=9, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    in_stock_total = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)


class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_qty = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    add_on = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    joining_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.DecimalField(max_digits=9, decimal_places=2)
    added_on = models.DateTimeField(auto_now_add=True)


class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)


class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    prod_details = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)


class CarrierAccount(models.Model):
    choices = ((1, "Debit"), (2, "Credit"), (3, "VND"))
    id = models.AutoField(primary_key=True)
    carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choices, max_length=255)
    transaction_amt = models.CharField(max_length=255)
    transaction_date = models.DateField()
    payment_mode = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


class CarrierBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc_no = models.CharField(max_length=255)
    Carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)


class EmployeeBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    ifsc_no = models.CharField(max_length=255)
    empoloyee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateTimeField()

