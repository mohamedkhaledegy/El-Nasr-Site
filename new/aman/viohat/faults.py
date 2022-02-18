from datetime import datetime
from multiprocessing import context
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count 
from django.db.models import Q
from aman.forms import *
from aman.filters import *

def fault_list(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    faults = Fault.objects.all()
    if request.GET:
        if profile.pos_site == 'Admin':
            faults_filter = FaultFilterAdmen(request.GET)
            faults = faults_filter.qs
        elif profile.pos_site == 'Staff':
            faults_filter = FaultFilterAdmen(request.GET)
            faults = faults_filter.qs
        else :
            faults_filter = FaultFilter(request.GET)
    else:
        faults_filter = FaultFilterAdmen()
        faults = Fault.objects.all().order_by('-fixed_at')
    stores = Store.objects.all()
    context = {
        'faults':faults,
        'fault_form':faults_filter,
        'stores':stores,
    }
    return render(request,'fault/fault-list.html',context)

def fault_detail(request,id_fault):

    pass

def fault_new(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
        if profile.pos_in_store == 'Admin':
            form = FaultFormAdmen()
        elif profile.pos_in_store == 'Staff':
            form = FaultFormStaff()
    else:
        form = None
        profile = None
    if request.POST:
        faults_form = form(request.GET)
    else:
        faults_form = form
    context={
            'form_new_fault': faults_form,
            }
    return render(request,'fault/fault-new.html',context)

def fault_edit(request):
    pass

def fault_list_new(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
        if profile.pos_in_store == 'Admin':
            form = FaultFormAdmen()
        elif profile.pos_in_store == 'Staff':
            form = FaultFormStaff()
        elif profile.pos_in_store == 'Manager':
            form = FaultForm()
    
    context = {
        'form':form,
        
    }
    faults = Fault.objects.all()
    return render(request,'fault/fault-list-new.html',context)