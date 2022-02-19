from datetime import datetime
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count 
from django.db.models import Q
from aman.forms import *
from aman.filters import *

def unit_list(request):
    units = StoreUnit.objects.all()

    context = {
        'units':units
    }

    return render(request,'units/list.html',context)

def unit_detail(request,unit_id):
    unit = get_object_or_404(StoreUnit,id=unit_id)
    context = {
        'unit':unit,
    }
    return render(request,'units/detail.html',context)

def order_unit_list(request):
    orders = OrderStoreUnit.objects.all()
    context = {
        'orders':orders,
    }
    return render(request , 'units/order/list.html',context)