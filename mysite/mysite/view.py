from django.shortcuts import render
from django.http import HttpResponse

def store(request):
    return render(request,"Store.html")

def cart(request):
    return render(request,"Cart.html")

def checkout(request):
    return render(request,"Checkout.html")

def aboutus(request):
    return render(request,"Aboutus.html")

def collect(request):
    print(request.POST)
    name = request.POST['name']
    return render(request,"new.html",{'name':name})

def disinfectants(request):
    return render(request,"Disinfectants.html")

def sanitizers(request):
    return render(request,"Sanitizers.html")

def Households(request):
    return render(request,"Households.html")

def cosematics(request):
    return render(request,"Cosematics.html")