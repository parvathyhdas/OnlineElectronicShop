from django.shortcuts import render,redirect
from ShopApp.models import ShopDB,CategoryDB,ProductDB
from Frontend.models import ContactDB
from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def indexPage(reg):
    return render(reg,"index.html")

def addShop(reg):
    return render(reg,"addShop.html")

def saveshop(reg):
    if reg.method == "POST":
        na = reg.POST.get("name")
        em = reg.POST.get("email")
        pas = reg.POST.get("password")
        loc = reg.POST.get("location")
        ad = reg.POST.get("address")
        im = reg.FILES["image"]
        obj = ShopDB(Name=na,Email=em,Password=pas,Location=loc,Address=ad,Image=im)
        obj.save()
        return redirect(addShop)

def addCategory(reg):
    return render(reg,"AddCategory.html")

def saveCategory(reg):
    if reg.method == "POST":
        na = reg.POST.get("catname")
        des = reg.POST.get("description")
        img = reg.FILES["image"]
        obj = CategoryDB(CategoryName=na,Description=des,CategoryImage=img)
        obj.save()
        messages.success(reg,"category saved successfully..!")
        return redirect(addCategory)

def displayCategory(reg):
    data = CategoryDB.objects.all()
    return render(reg,"displaycategory.html",{'data':data})

def editCategory(reg,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(reg,"editCategory.html",{'data':data})

def updateCategory(reg,dataid):
    if reg.method == "POST":
        na = reg.POST.get("catname")
        des = reg.POST.get("description")
        try:

            img = reg.FILES["image"]
            fs =FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =CategoryDB.objects.get(id=dataid).CategoryImage
        CategoryDB.objects.filter(id=dataid).update(CategoryName=na,Description=des,CategoryImage=file)
        messages.success(reg, "category update successfully..!")
        return redirect(displayCategory)

def deleteCategory(reg,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.success(reg, "category delete successfully..!")
    return redirect(displayCategory)

def AddProduct(reg):
    cat = CategoryDB.objects.all()
    return render(reg,"AddProduct.html",{'cat':cat})

def saveProduct(reg):
    if reg.method == "POST":
        cname = reg.POST.get("catname")
        pname = reg.POST.get("pname")
        des = reg.POST.get("description")
        pri = reg.POST.get("price")
        img = reg.FILES["image"]
        obj = ProductDB(CategoryName=cname,ProductName=pname,Description=des,Price=pri,ProductImage=img)
        obj.save()
        messages.success(reg, "Product saved successfully..!")
        return redirect(AddProduct)

def displayProduct(reg):
    prodcut = ProductDB.objects.all()
    return render(reg,"displayProduct.html",{'prodcut':prodcut})

def editProduct(reg,dataid):
    data = ProductDB.objects.get(id=dataid)
    cat = CategoryDB.objects.all()
    return render(reg,"editProduct.html",{'data':data,'cat':cat})

def updateProduct(reg,dataid):
    if reg.method == "POST":
        cname = reg.POST.get("catname")
        pname = reg.POST.get("pname")
        des = reg.POST.get("description")
        pri = reg.POST.get("price")
        try:
            img = reg.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).ProductImage
        ProductDB.objects.filter(id=dataid).update(CategoryName=cname,ProductName=pname,Description=des,Price=pri,ProductImage=file)
        messages.success(reg, "Product update successfully..!")
        return redirect(displayProduct)

def deleteProduct(reg,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    messages.success(reg, "Product delete successfully..!")
    return redirect(displayProduct)

def adminLogin(reg):
    return render(reg,"adminLogin.html")

def adminLoginPage(request):
    if request.method == "POST":
        na = request.POST.get("name")
        pwd = request.POST.get("password")
        if User.objects.filter(username__contains=na).exists():
            user = authenticate(username=na,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = na
                request.session['password'] = pwd
                return redirect(indexPage)
            else:
                return redirect(adminLogin)
        else:
            return redirect(adminLogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminLogin)


def displayContact(request):
    data = ContactDB.objects.all()
    return render(request,"displayContact.html",{'data':data})

def deleteContact(reg,dataid):
    data = ContactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayContact)

