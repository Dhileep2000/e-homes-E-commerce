from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *

from product.models import Product, Category

def homepage(request):
    products = Product.objects.all()[0:8]

    return render(request,'home.html', {'products': products})


def signuppage(request):
    
     if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
     else:
        form = SignUpForm()


     return render(request,'signup.html',{'form': form})
 
 
 
@login_required 
def myaccount(request):
    return render(request,'myaccount.html')


@login_required 
def edit_myaccount(request):
    
    if request.method == 'POST':
        
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email =  request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()
        return redirect('myaccount')
    
    return render(request,'edit_myaccount.html')



def loginpage(request):

    return render(request,'login.html')


def logoutpage(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
        return redirect("/")




def shoppage(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'shop.html', context)