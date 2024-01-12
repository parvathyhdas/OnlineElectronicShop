from django.shortcuts import render,redirect
from ShopApp.models import CategoryDB,ProductDB
from Frontend.models import ContactDB,RegisterDB,CartDB
from django.contrib import messages

# Create your views here.
def homePage(request):
    cat = CategoryDB.objects.all()
    return render(request,"home.html",{'cat':cat})

def productStore(request):
    pro = ProductDB.objects.all()
    return render(request,"product.html",{'pro':pro})

def single_productPage(request,proid):
    data = ProductDB.objects.get(id=proid)
    return render(request,"single_product.html",{'data':data})

def productFiltered(request,cat_name):
    data = ProductDB.objects.filter(CategoryName=cat_name)
    return render(request,"Product_filtered.html",{'data':data})

def aboutPage(reg):
    return render(reg,"aboutUs.html")

def contactPage(reg):
    return render(reg,"contact.html")

def services(reg):
    return render(reg,"services.html")

def saveContact(request):
    if request.method == "POST":
        na =request.POST.get("name")
        em =request.POST.get("email")
        me =request.POST.get("message")
        obj = ContactDB(Name=na,Email=em,Message=me)
        obj.save()
        messages.success(request, "Contact saved successfully..!")
        return redirect(contactPage)

def RegisterPage(reg):
    return render(reg,"Register.html")

def saveRegister(reg):
    if reg.method == "POST":
        na = reg.POST.get("name")
        mob = reg.POST.get("mobile")
        em = reg.POST.get("email")
        us = reg.POST.get("username")
        pa = reg.POST.get("password")
        obj =RegisterDB(Name=na,Mobile=mob,Email=em,UserName=us,Password=pa)
        obj.save()
        messages.success(reg, "Registration successfully done..!")
        return redirect(RegisterPage)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pwd = request.POST.get("password")
        if RegisterDB.objects.filter(UserName=un,Password=pwd).exists():
            request.session['UserName'] = un
            request.session['Password'] = pwd
            messages.success(request, "Login successfully ...")
            return redirect(homePage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(RegisterPage)
    return redirect(RegisterPage)

def UserLogout(request):
    del request.session['UserName']
    del request.session['Password']
    messages.success(request, "Logout successfully ..")
    return redirect(UserLogin)

def cartPage(request):
    data = CartDB.objects.filter(UserName=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price+i.Totalprice
    return render(request,"cartPage.html",{'data':data,'total_price':total_price})

def saveCart(reg):
    if reg.method == "POST":
        na = reg.POST.get("username")
        pn = reg.POST.get("pname")
        des = reg.POST.get("description")
        qty = reg.POST.get("qty")
        pr = reg.POST.get("total")
        obj = CartDB(UserName=na,ProductName=pn,Description=des,Quantity=qty,Totalprice=pr)
        obj.save()
        messages.success(reg, "Add Product successfully..!")
        return redirect(cartPage)

def deletecart(reg,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    messages.error(reg, "Remove Product ..!")
    return redirect(cartPage)

def checkoutPage(request):
    data = CartDB.objects.filter(UserName=request.session['UserName'])
    total = 0
    for i in data:
        total = total+i.Totalprice
    return render(request,"checkout.html",{'data':data,'total':total})