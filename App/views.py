from django.shortcuts import render
#My Imports
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Staff
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Function to render the HomePage
def frontend(request):
    return render(request,'frontend.html')

# Function to render the backend Page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):

    if 'q' in request.GET:
        q = request.GET['q']
        all_staff_list = Staff.objects.filter(
              Q(first_name__icontains=q) |   Q(last_name__icontains=q) |  Q(mobile__icontains=q) |  Q(card_id_no__icontains=q) |  Q(email__icontains=q) |  Q(gender__icontains=q) |  Q(age__icontains=q)
        ).order_by('-created_at')
    else:
        all_staff_list = Staff.objects.all().order_by('-created_at')
    paginator = Paginator(all_staff_list,10)
    page = request.GET.get('page')
    all_staff = paginator.get_page(page)
    return render(request,'backend.html',{'staffs':all_staff})

# Function to insert new staff
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def add_staff(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('mobile') and request.POST.get('card_id_no') and request.POST.get('birthdate') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('bloodgrp') and request.POST.get('email') and request.POST.get('address'):
            staff = Staff() 
            staff.title =   request.POST.get('title')
            staff.first_name =   request.POST.get('first_name')            
            staff.last_name =   request.POST.get('last_name')
            staff.mobile =   request.POST.get('mobile')        
            staff.card_id_no =   request.POST.get('card_id_no')
            staff.birthdate =   request.POST.get('birthdate')            
            staff.age =   request.POST.get('age')            
            staff.gender =   request.POST.get('gender')
            staff.bloodgrp =   request.POST.get('bloodgrp')            
            staff.email =   request.POST.get('email')   
            staff.address =   request.POST.get('address') 
            staff.save() 
            messages.success(request,'Staff ' + staff.first_name + ' added successfully !')
            return HttpResponseRedirect('backend')
    else:
            return render(request,'add_staff.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
@login_required(login_url="login")
def edit_staff(request, staff_id):
    staff = Staff.objects.get(id = staff_id)
    print(staff.birthdate)
    if staff != None:
       return render(request,"edit_staff.html",{'staff':staff})
       
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def save_staff(request):
    if request.method == "POST": 
       staff = Staff.objects.get(id = request.POST.get('id'))  
       if staff != None:                  
            staff.title = request.POST.get('title')
            staff.first_name = request.POST.get('first_name')   
            staff.last_name = request.POST.get('last_name')
            staff.mobile = request.POST.get('mobile')                
            staff.card_id_no = request.POST.get('card_id_no')
            staff.birthdate = request.POST.get('birthdate')            
            staff.age = request.POST.get('age')   
            staff.gender = request.POST.get('gender')
            staff.bloodgrp = request.POST.get('bloodgrp')            
            staff.email = request.POST.get('email') 
            staff.address = request.POST.get('address')   
            staff.save()    

            messages.success(request, "Staff update successfullty !") 
            return HttpResponseRedirect('backend')

# Function to remove staff       
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_staff(request, staff_id):
    staff = Staff.objects.get(id = staff_id)
    staff.delete()

    messages.success(request, "Staff remove successfullty !") 
    return HttpResponseRedirect('backend')



