from asyncio import sslproto
from datetime import datetime
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count 
from aman.forms import *
from aman.filters import *

def visits_list(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    
    stores_all = Store.objects.all()
    visits_all = Visit.objects.all().order_by('-date_created')
    faults_all = Fault.objects.all().order_by('-created_at')

    if profile.pos_in_store == 'Quality':
        stores = stores_all
        visits = visits_all
        faults = faults_all
        stores_count = stores.count()
        visits_count = visits.count()
        faults_count = faults.count()
    elif profile.pos_in_store == 'Manager':
        stores = stores_all
        visits = visits_all
        faults = faults_all
        stores_count = stores.count()
        visits_count = visits.count()
        faults_count = faults.count()
    elif profile.pos_in_store == 'Admin':
        stores = stores_all.filter(user_admin=request.user)
        visits = visits_all.filter(store__in=stores)
        faults = faults_all.filter(belong_to__in=stores)
        form = VisitFilterAdmen()
        stores_count = stores.count()
        visits_count = visits.count()
        faults_count = faults.count()
    else :
        stores = stores_all
        visits = visits_all
        faults = faults_all
        stores_count = stores.count()
        visits_count = visits.count()
        faults_count = faults.count()

    if request.GET:
        form = VisitFilterAdmen(request.GET)
        visits = form.qs
    else:
        form = VisitFilterAdmen()

    context = {
        'form':form,
        'stores':stores,
        'visits':visits,
        'visits_count':visits_count,
        'count_stores':stores_count,
        'faultss':faults,
        }
    return render(request,'visit/list.html',context)

        
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
