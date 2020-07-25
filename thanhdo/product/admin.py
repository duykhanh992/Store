from django.contrib import admin
from .models import Category,Carrier,Product,ProductDetails,Employee,Customer,Bill,EmployeeSalary,BillDetails,CustomerRequest,CarrierAccount,CarrierBank,EmployeeBank
# Register your models here.
admin.site.register(Carrier)
admin.site.register(Product)
admin.site.register(ProductDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
