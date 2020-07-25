from django.shortcuts import render
from product.models import Customer

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {"name" : "Thanh Do"})

# def home(request):


#     return render(request, 'home.html')

def formview(request):
    return render(request,'form.html')

def employeeview(request):
    name = request.POST['firstname'] +' '+ request.POST['lastname']
    return render(request,'result.html', {'result':name})

def Customerview(request):
    cust = Customer.objects.all()
    return render(request,"home.html", {'cust':cust})