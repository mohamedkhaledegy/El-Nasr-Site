from asyncio import sslproto
from datetime import datetime
from multiprocessing import context
from wsgiref.util import request_uri
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
    visits_all = Visit.objects.all().order_by('-date_visit')
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
        visits = visits_all

    context = {
        'form':form,
        'stores':stores,
        'visits':visits,
        'visits_count':visits_count,
        'count_stores':stores_count,
        'faultss':faults,
        }
    return render(request,'visit/list.html',context)


def new_visit_emergency(request,slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None

    stores = Store.objects.all()
    store = get_object_or_404(Store,slug=slug)
    form = FaultFormAdmen()
    if request.method == "POST":
        form = FaultFormEmergency(request.POST)
        if form.is_valid():
            #store = VisitForm(request.POST)
            #print(store)
            form_instance = form.save(commit=False)
            form_instance.belong_to = store
            form_instance.created_by = profile
            form_instance.status = True
            form_instance.save()
            print('Success')
            return redirect('/visit/list/')
        else:
            form = FaultFormEmergency()
    else:
        form = FaultFormEmergency()
        # fields = ['store','short_desc',
        # 'describe_proplem','argent',
        # 'faults'
        # ]
    form.store = store

    print(form)

    context = {
        'store':store,
        'stores':stores,
        'form':form
    }
    return render(request,'visit/new_visit_emergency.html',context)


def visit_fault_edit(request,visit_id,fault_id):
    visit = get_object_or_404(Visit,id=visit_id)
    fault = get_object_or_404(Fault,id=fault_id)

    print(visit)
    print(fault)
    form_fault = FaultFormAdmen(instance=fault)
    form_visit = VisitFaultFormAdmen(instance=visit)

    print(request.GET)
    if 'fault_nn' in request.GET:
        print(request.GET['fault_nn'])


    ### دى عشان اضيف كذا فورم وكل فورم وارثة من الاوبجكت
    # forms_faults = []
    # faults = Fault.objects.filter(visit=fault.visit)
    # for form in faults:
    #     fault_form = FaultVisitFormAdmen(instance=form)
    #     forms_faults.append(fault_form)
    # print(len(forms_faults))

    if request.POST:
        pass
        form_fault = FaultFormAdmen(request.POST)
        if form_fault.is_valid():
            form_fault.save(commit=False)
            if form_fault.created_by != None:
                print('Created By T')

    context = {
        'visit':visit,
        'fault':fault,
        'form_faults':form_fault,
        'form_visit':form_visit,
    }

    return render(request,'profile/partial_manage/visit_fault_edit_form.html',context)