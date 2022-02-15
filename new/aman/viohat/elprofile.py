from datetime import datetime
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count 
from django.db.models import Q
from aman.forms import *
from aman.filters import *

def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    
    stores = Store.objects.all()
    store_admin = Store.objects.filter(user_admin=profile.user)

    
    ## عدد فروع الاددمين
    num_of_admin_stores = store_admin.count()

    ## الشهر
    this_month = datetime.now().month
    
    ## فلتر لزيارات الشهر
    visit_filter = Visit.objects.filter(date_visit__month=this_month,send_by=request.user.id)
    
    ## فلتر الأعطال

    fault_filter = Fault.objects.filter(created_at__month=this_month,belong_to__in=store_admin)
    if fault_filter.count() >= 0:
        print(fault_filter)    
    print("Visit Filters count is >>")
    print(visit_filter.count())
    print("Fault Filters count is >>")
    print(fault_filter.count())
    context = {
        #### محتويات البروفايل

        'profile':profile, ## جيع معلومات البروفايل
        'stores':stores, ## الفروع كاملة
        'stores_user':store_admin,  ## فروع الادمين
        'num_of_admin_stores':num_of_admin_stores, ## عدد فروع الادمين
        'this_month':this_month, ### الشهر الحالى
        'visits_this_month':visit_filter, ### الزيارات لفروع الادمن
        'faults_this_month':fault_filter, ### الاعطال لفروع الادمن

    }
    return render(request,'profile/profile.html',context)
