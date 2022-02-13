from datetime import datetime
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
    faults_filter = FaultFilter()
    if request.GET:
        faults_filter = FaultFilter(request.GET)
        faults_filter = FaultFilter(created_by=request.user.id)
        faults = faults_filter.qs
    else:
        faults_filter = None
        store_filter = FaultFilter().order_by('')
    stores = Store.objects.all()
    context = {
        'faults':faults,
        'fault_form':faults_filter,
        'stores':stores,
        
    }
    return render(request,'fault/fault-list.html',context)

def fault_detail(request):
    pass

def fault_new(request):
    pass

def fault_edit(request):
    pass

