from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
import socket
import datetime

# Create your views here.
def home(request):
    subscribers = list(Subscriber.objects.all())
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        for subscriber in subscribers:
            if subscriber.email == sub_email:
                print('You have already subscribed to our Newsletter.')
                break 
            
        else:
            sub = Subscriber(email=sub_email)
            sub.save()
        
        
        # try:
        #     send_mail('Chat message', message, {request.user.email},
        #         ['muzarabanicarson@gmail.com'], fail_silently=False)

        # except socket.gaierror as e:
        #     return redirect('chat')
    
    return render(request, 'main/index.html')

def send_email(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # email_from = email
        recipient_list = ['muzarabanicarson@gmail.com']
        
        try:
            if name and email and subject and message != "":
                interaction = EmailInteractions(name=name,phone=number,email=email,subject=subject,message=message)
                interaction.save()
                send_mail(subject, message, email,
                        recipient_list, fail_silently=False)
                messages.success(
                request, ("Your email has been sent successfully \n we will get back to you as soon as we can"))
                
                # interaction = EmailInteractions(name=name,number=number,email=email,subject=subject,message=message)
                # interaction.save()
                return redirect("home")
            else:
                messages.error(
                    request, ("Enter all the required info")
                )

        except socket.gaierror as e:
            messages.error(
                request, ("Message not sent")
            )
            return redirect('home')
    return render(request, 'main/index.html')


def service(request):
    return render(request, 'main/services.html')


def couch(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Couch':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/couch.html', context)
    except:
        return render(request, 'main/couch.html')

def headboard(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Headboard':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/headboard.html', context)
    except:
        return render(request, 'main/headboard.html')

def chair(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Chair':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/chairs.html', context)
    except:
        return render(request, 'main/chairs.html', context)

def ottoman(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Ottoman':
                productList.append(product)
                
                context={'productList': productList}
                
        return render(request, 'main/ottomans.html', context)
    except:
        return render(request, 'main/ottomans.html')

def blanket_box(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Blanket box':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/blanket_boxes.html', context)
    except:
        return render(request, 'main/blanket_boxes.html')

def lamp_shade(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Lamp shade':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/lamp_shades.html', context)
    except:
        return render(request, 'main/lamp_shades.html', context)
    

def curtain(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Curtain':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/curtains.html', context)
    except:
        return render(request, 'main/curtains.html', context)
        

def cushion(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Cushion':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/cushions.html', context)
    except:
        return render(request, 'main/cushions.html')
    

def scatter_cushion(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Scatter cushion':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/scatter_cushions.html', context)
    except:
        return render(request, 'main/scatter_cushions.html')
        

def roman_blind(request):
    try:
        products=list(Product.objects.all())
        productList = []
        for product in products:
            if product.product_type == 'Roman blind':
                productList.append(product)
                
                context={'productList': productList}
        return render(request, 'main/roman_blinds.html', context)
    except:
        message = "Empty"
        return render(request, 'main/roman_blinds.html', {'message': message})
        
    

def blog(request):
    return render(request, 'main/blog.html')

def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you, your review has been successfully submitted.')
            
            return redirect('add_testimony')
        
    else:
        form = TestimonyForm()
        return render(request, 'main/add_testimony.html', {'form': form})
        
    

def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials}
    return render(request, 'main/testimonials.html', context)

@login_required
def dashboard(request):
    all_clients = Client.objects.all()
    
    context = {'all_clients': all_clients}
    return render(request, 'main/dashboard/index.html', context)

@login_required
def viewJobCards(request):
    return render(request, 'main/dashboard/viewJobCards.html')

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you, your review has been successfully submitted.')
            
            return redirect('add_job')
        
    else:
        form = JobForm()
        return render(request, 'main/dashboard/addJob.html', {'form': form})
    
    return render(request, 'main/dashboard/addJob.html', {'form': form})
        

@login_required
def allJobs(request):
    all_jobs = Job.objects.all()
    
    context = {'all_jobs': all_jobs}
    return render(request, 'main/dashboard/all_jobs.html', context)

@login_required
def job_cards(request):
    return render(request, 'main/job_cards.html')

def inventory(request):
    items = Inventory.objects.all()
    
    if request.method == "POST":
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        
        newItem = Inventory(item = item, quantity = quantity)
        newItem.save()
        
    context = {'items': items}
    return render(request, 'main/dashboard/inventory.html', context)


def client(request):
    all_clients = Client.objects.all()
    
    
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        if len(phone) > 9 and len(phone) < 9:
            print("Phone number must be less than 10.")
        
        
        # newClient = Client(name=name, surname=surname,phone=phone,email=email)
        # newClient.save()
        
    context = {'all_clients': all_clients}
    
    return render(request, 'main/dashboard/clients.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your image has been successfully uploaded')
            
            return redirect('add_product')
        
    else:
        form = ProductForm()
        return render(request, 'main/dashboard/add_product.html', {'form': form})


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(username=username).exists(): 
                messages.info(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                
                
            else:
                user = User.objects.create_user(username=username, password=password1, email = email)
                user.set_password(password1)
                user.save()
                
                user = authenticate(username=username, password=password1)

                if user is not None:
                    login(request, user)
                    if request.GET.get('next', None):
                        return HttpResponseRedirect(request.GET['next'])
                else:
                    messages.error(request, 'Invalid username or password')

                return redirect('dashboard')
        else:
            messages.info(
                request, ("Passwords didn't match. Try again.")
            )
        
    return render(request, 'main/dashboard/register.html')


def loginUser(request):
    user_ids = list(LoginId.objects.all())
    staff_ids = []
    for staff_id in user_ids:
        staff_ids.append(staff_id.user_id)
    
    
    userId = request.POST.get('user_id')
    
    if request.method == "POST":
        userId = request.POST.get('user_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if userId in staff_ids:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET['next'])
            else:
                messages.error(request, 'Invalid username or password')
                
            return redirect('dashboard')
        else:
            messages.error(request, "Staff id doesn't exist")


    return render(request, 'main/dashboard/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')
