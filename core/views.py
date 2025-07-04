from django.shortcuts import render , redirect
from .models import product  , category , Profile
from django.contrib.auth import authenticate , login , logout  
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from django import forms  
from .forms import SignUpForm , UpdateUserForm , ChangePasswordForm ,UserInfoForm
from django.db.models import Q
import json
from card.Card import Card
from payment.forms import PostingForm
from payment.models import PostingAddress


# Create your views here.
def home(request):
    products = product.objects.all() 
    return render(request , 'home.html' , {'products' : products})  

# about page
def About(request):
    return render(request , 'About.html' , {} )   

# login page 
def login_user(request):
    if request.method == "POST":
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password') 
        user = authenticate(request , username = username ,password = password) 
        if user is not None :
            login(request , user)

            current_user = Profile.objects.get(user_id=request.user.id)
            # get saved cart from the database
            saved_cart = current_user.old_cart
            # convert database string into python dictionary
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                # added the loaded dictionary
                cart = Card(request)
                for key , value in converted_cart.items():
                    cart.db_add(product=key , quantity= value)
            messages.success(request , ("You have been logged in successfully"))  
            return redirect('home') 
        else :
            messages.success(request , ("Login failed , Please try again."))   
            return redirect('login') 
    else :
        return render(request ,'login.html' , {} ) 

#  logout page 
def logout_user(request):
    logout(request)  
    messages.success(request , ("You have been logged out successfully")) 
    return redirect('home')  

def register_user(request):
    form = SignUpForm() 
    if request.method == "POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  
            user = authenticate(request , username = username ,password = password)  
            if user is not None:
                login(request , user) 
                messages.success(request , "You have been registered successfully") 
                return redirect("home") 
            else:
                messages.error(request , "Registration succeeded, but login failed.")
                return redirect("login")
        else:
            messages.error(request , "Registration failed, please try again.")
            return redirect("register")
    else: 
        return render(request , 'register.html' , {'form' : form})

def product_detail(request , pk) : 
    product_obj = product.objects.get(id = pk)
    return render(request , 'product.html' , {'product' : product_obj})  


def category_summary(request):
    categories = category.objects.all()
    return render(request , 'category_summary.html' , {"categories" : categories})

def category_detail(request , sth):  
    
    # replace hyphens with spaces
    sth = sth.replace('-' , ' ')
     
    # grab the category from the url 
    try :
        category_obj = category.objects.get(name__iexact=sth)
        product_obj = product.objects.filter(category = category_obj) 
        return render(request , 'category.html' , {'product' : product_obj , 'category' : category_obj} )
    except :
        messages.success(request , ('Category does not exist.'))    
        return redirect('home') 

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None , instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request , current_user)
            messages.success(request, "User information has been Updated")
            return redirect("home")
        return render(request, "update_user.html" , {"user_form" : user_form})
    else:
        messages.success(request, "You must be logged in to access this page.")
        return redirect("home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method=="POST":
            form = ChangePasswordForm(current_user , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , "Your Password has been updated...")
                login(request , current_user)
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request , error)
                    return redirect("update_password")
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form': form})
    else:
        messages.success(request , "Error , you are not logged in")
        return redirect("home")


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        # get posting info
        posting_user = PostingAddress.objects.get(user__id=request.user.id)
        # get posting form

        form = UserInfoForm(request.POST or None , instance=current_user)
        posting_form = PostingForm(request.POST or None, instance=posting_user)
        if form.is_valid() or posting_form.is_valid():
            # save original form
            form.save()
            # save posting form
            posting_form.save()


            messages.success(request, "User information has been Updated")
            return redirect("home")
        return render(request, "update_info.html" , {"form" : form , 'posting_form' : posting_form})
    else:
        messages.success(request, "You must be logged in to access this page.")
        return redirect("home")


def search (request):
    if request.method == "POST":
        searched = request.POST["searched"]
        searched = product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        # test for null
        if not searched:
            messages.success(request , "No Product with such name is available in our Shop , Please try again")
            return render(request , "search.html" , {})
        else:
            return render(request, "search.html", {"searched": searched})
    else:
        return render(request, "search.html", {})