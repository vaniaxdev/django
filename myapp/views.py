from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import request
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Product
from myapp.my_forms import ProductForm


# Create your views here.
@login_required
def home(request):
    print("Home")
    products = Product.objects.all() # select everything from products
    for product in products:
        print(product.name, product.price)
    return render(request, "home.html", {"products": products})

@login_required
def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f" {form.name} successfully added")
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, "add.html", {"form": form})

   # Product.objects.get_or_create(name="Unga",
    #                       code="0100899",
     #                      price=560.0,
     #                      cost=488.0,
      #                    for_sale=False
       #                    )
    #Product.objects.get_or_create(name="Mango Juice",
        #                  price=450.0,
         #                  cost=350.0,
          #                 category="Foods",
           #                for_sale=True
             #              )
    #Product.objects.get_or_create(name="Biscuit",
                         #  code="0100901",
                          # price=300.0,
                           #cost=200.0,
                           #category="Foods",
@login_required                          #)
def delete_product(request, id):
    product = Product.objects.get(id=id)  #  select everything from products where id=65
    product.delete() # delete from products where id=65
    messages.warning(request, f"{product.name} deleted permanently")
    return redirect('home')


@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name} successfully updated")
            return redirect('home')
    else:
        form = ProductForm(instance=product)

    return render(request, "edit.html", {"form": form})


@login_required
def details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "details.html", {"product": product})


def signin():
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, f"Successfully Logged In")
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'reqistration/login.html', {'form': form})




def signup():

    return None







@login_required
def signout():
    if request.method == "POST":
        logout(request)
    return redirect('login')


